from django.core.mail import EmailMessage
from core.utils.monitor_utils import log

SUBJECT = "Contract Review Upcoming"
BODY = "This is to inform you of a looming contract expiry. Kindly login at contracts.nssfug.org to view recent " \
       "notifications. "
FROM = "contracts@nssfug.org"
to = 'karuhanga475@gmail.com'


def send_email(to=to, cc=[], subject=SUBJECT, body=BODY):
    # try:
    email = EmailMessage(to=[to], cc=cc, subject=subject, body=body, from_email=FROM)
    email.send()
    # except Exception as e:
    #     log(str(e))
