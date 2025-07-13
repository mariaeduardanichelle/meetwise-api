from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Registration

@receiver(post_save, sender=Registration)
def enviar_email_Registration(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        event = instance.event

        send_mail(
            subject=f"Inscrição confirmada: {event.name}",
            message=f"Olá {user.first_name}, sua inscrição no event '{event.name}' foi confirmada!",
            from_email="noreply@seusite.com",
            recipient_list=[user.email],
            fail_silently=False,
        )