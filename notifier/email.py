from django.core.mail import EmailMessage
from core.utils.monitor_utils import log

SUBJECT = "Contract Review Upcoming"
BODY = "This is to inform you of a looming contract expiry. Kindly login at contracts.nssfug.org to view recent " \
       "notifications. "
FROM = "contracts@nssfug.org"


def send_email(to, subject=SUBJECT, body=BODY):
    try:
        email = EmailMessage(to=[to], subject=subject, body=body)
        email.send()
    except Exception as e:
        log(str(e))
