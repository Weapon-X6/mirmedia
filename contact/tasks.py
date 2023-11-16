from celery import shared_task
from django.core.mail import EmailMessage
from celery.utils.log import get_task_logger
from django.conf import settings

logger = get_task_logger(__name__)


@shared_task
def send_email(email, name, content):
    logger.info(f"SENDING EMAIL: {email}, {name}, {content}")
    message = EmailMessage(
        subject=name,
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[
            settings.EMAIL_SEND_TO,
        ],
        reply_to=[email],
    )
    message.send(fail_silently=False)
