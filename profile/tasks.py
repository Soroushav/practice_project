from celery.utils.log import get_task_logger
import config.settings
from .email import create_user_sent_email
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage

Users = get_user_model()
logger = get_task_logger(__name__)


@shared_task()
def create_user_sent_email_task(username, email):
    logger.info("Sent SignUp Email")
    return create_user_sent_email(username, email)


@shared_task()
def user_sent_if_ok():
    logger.info("Sent Users an Email")
    for user in Users.objects.all():
        email = user.email
        username = user.username
        body = f'Choni {username} hawal naprsi'
        message = EmailMessage(from_email=config.settings.DEFAULT_FROM_EMAIL,
                               to=[email, ],
                               body=body,
                               subject="Hawal")
        message.send(fail_silently=False)
    return "done"
