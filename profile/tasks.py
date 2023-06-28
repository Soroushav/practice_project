from celery.utils.log import get_task_logger
from .email import create_user_sent_email
from celery import shared_task
logger = get_task_logger(__name__)


@shared_task()
def create_user_sent_email_task(username, email):
    logger.info("Sent SignUp Email")
    return create_user_sent_email(username, email)