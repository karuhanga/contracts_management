from datetime import date, timedelta
from core.utils.monitor_utils import log
from .email import send_email

from core.models import Contract
from .models import NotificationPoint, NotificationStatus

TODAY = ''  # Holds today's date
DATES = []  # Holds calculated dates based on notification_points


# provides interface to access generated dates
# uses global DATES variable
# args - an index
# returns - a date from DATES
# logs - No
def get_date(i):
    global DATES
    try:
        return DATES[i]
    except IndexError:
        return TODAY  # TODO Improve this


# send email notification to concerned parties
# args - notification_point; that triggered this, contract; whose expiry is pending
# returns - None
# logs - No
def generate_body(notification_point, contract):
    return "This is to inform you of a looming contract expiry.\nDetails:\n" + contract + "\n\nThis contract expires in " + notification_point


def generate_subject(notification_point):
    return "Contract Review due in " + notification_point


def notify(notification_point, contract):
    subject = generate_subject(notification_point)
    body = generate_body(notification_point, contract)
    to = contract.contract_manager.email
    # bcc TODO Implement optional carbon copy to manager

    send_email(to, subject, body)


# notifies concerned party of expiry
# called if action not taken yet
# args - a contract
# returns - None
# logs - No
def notify_passed(contract):
    subject = "Contract Review Overdue"
    body = "Details: \n" + contract
    to = contract.contract_manager.email
    # bcc TODO Implement optional carbon copy to manager

    send_email(to, subject, body)


# generates dates based on arg(notification_points)
# updates global variable DATES
# args - user defined notification_points
# returns - None
# logs - No
def generate_dates(notification_points):
    global DATES, TODAY

    for notification_point in notification_points:
        DATES.append(TODAY + timedelta(days=notification_point.when_time_left))


# determines appropriate notification for each pending contract expiry
# alerts of expired contract if action not taken yet
# args - a contract, user defined notification points
# returns - None
# logs - Yes
def check_notify(contract, notification_points):
    if TODAY > contract.expiry_date:
        status = NotificationStatus.objects.get_or_create(contract=contract)
        if status.action_taken:
            log("Notification was cancelled")
        else:
            notify_passed(contract)
        return

    for i in range(0, len(notification_points)):
        date_to_check = get_date(i)
        if date_to_check > TODAY:
            notify(notification_points[i], contract)
            return

    log("No notifs at this time")


# gets user defined reminder times and generates dates from today
# calls check_notify for each contract
# args - None
# returns - None
# logs - No
def run_due_checker():
    global TODAY

    notification_points = NotificationPoint.objects.order_by('when_time_left').all()

    if len(notification_points) == 0:
        log("No notification points added")
        return

    TODAY = date.today()

    generate_dates(notification_points)

    contracts = Contract.objects.all()  # TODO Improve number of items that are fetched

    for contract in contracts:
        check_notify(contract, notification_points)


# If command line run
if __name__ == '__main__':
    run_due_checker()
