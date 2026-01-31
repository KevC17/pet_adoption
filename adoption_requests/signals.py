from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

from .models import AdoptionRequest
from .services.email_service import (
    send_adoption_request_received,
    send_adoption_result_email,
)

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AdoptionRequest)
def adoption_email_signal(sender, instance, created, **kwargs):
    """
    Signal defensivo:
    - Nunca rompe el flujo
    - Usa user.email
    - Evita correos duplicados
    """

    try:
        user = instance.user

        if not user or not user.email:
            logger.warning(
                f"AdoptionRequest {instance.id} sin email de usuario."
            )
            return

        # 📨 Solicitud creada (PENDING)
        if created:
            if instance.last_email_sent == "RECEIVED":
                return

            try:
                send_adoption_request_received(instance)
                instance.last_email_sent = "RECEIVED"
                instance.save(update_fields=["last_email_sent"])
            except Exception as e:
                logger.error(
                    f"Error enviando email RECEIVED "
                    f"(AdoptionRequest {instance.id}): {e}"
                )
            return

        if instance.status in [
            AdoptionRequest.Status.APPROVED,
            AdoptionRequest.Status.REJECTED,
        ]:
            email_type = instance.status

            if instance.last_email_sent == email_type:
                return

            try:
                send_adoption_result_email(instance)
                instance.last_email_sent = email_type
                instance.save(update_fields=["last_email_sent"])
            except Exception as e:
                logger.error(
                    f"Error enviando email {email_type} "
                    f"(AdoptionRequest {instance.id}): {e}"
                )

    except Exception as fatal_error:
        logger.critical(
            f"Fallo inesperado en adoption_email_signal "
            f"(AdoptionRequest {instance.id}): {fatal_error}"
        )