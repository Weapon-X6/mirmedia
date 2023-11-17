from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactRequest
from .tasks import send_email


@receiver(post_save, sender=ContactRequest, dispatch_uid="contact_request_saved")
def contact_request_saved(sender, instance, created, **kwargs):
    if created:
        send_email.delay(instance.email, instance.name, instance.content)
