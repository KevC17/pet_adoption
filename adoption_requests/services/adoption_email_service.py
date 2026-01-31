from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_adoption_request_received(adoption):
    """
    Correo: Solicitud de adopción recibida
    """
    user = adoption.user

    if not user or not user.email:
        logger.warning(
            f"AdoptionRequest {adoption.id}: usuario sin email."
        )
        return

    subject = '🐾 Hemos recibido tu solicitud de adopción'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]

    text_content = (
        f'Hola {user.username},\n\n'
        f'Hemos recibido tu solicitud para adoptar a {adoption.pet.name}.\n'
        'Nuestro equipo la revisará pronto.'
    )

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #f9fafb; padding: 20px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td align="center">
              <table width="600" style="background: #ffffff; border-radius: 8px; padding: 30px;">

                <tr>
                  <td align="center" style="font-size: 28px; font-weight: bold; color: #111827;">
                    🐾 Puppy Family
                  </td>
                </tr>

                <tr><td height="20"></td></tr>

                <tr>
                  <td style="font-size: 16px; color: #374151;">
                    Hola <strong>{user.username}</strong>,
                  </td>
                </tr>

                <tr><td height="15"></td></tr>

                <tr>
                  <td style="font-size: 16px; color: #374151;">
                    Hemos recibido tu solicitud para adoptar a
                    <strong>{adoption.pet.name}</strong> 🐶🐱<br><br>
                    Nuestro equipo la revisará y te notificaremos muy pronto.
                  </td>
                </tr>

                <tr><td height="20"></td></tr>

                <tr>
                  <td style="font-size: 16px; color: #374151;">
                    Gracias por querer cambiar una vida ❤️
                  </td>
                </tr>

                <tr><td height="30"></td></tr>

                <tr>
                  <td style="font-size: 14px; color: #9ca3af;">
                    — Equipo Puppy Family 🐾
                  </td>
                </tr>

              </table>
            </td>
          </tr>
        </table>
      </body>
    </html>
    """

    try:
        email = EmailMultiAlternatives(subject, text_content, from_email, to)
        email.attach_alternative(html_content, "text/html")
        email.send()
    except Exception as e:
        logger.error(
            f"Error enviando correo RECEIVED (AdoptionRequest {adoption.id}): {e}"
        )


def send_adoption_result_email(adoption):
    """
    Correo: Solicitud aprobada o rechazada
    """
    user = adoption.user

    if not user or not user.email:
        logger.warning(
            f"AdoptionRequest {adoption.id}: usuario sin email."
        )
        return

    approved = adoption.status == adoption.Status.APPROVED

    subject = (
        "🎉 ¡Tu solicitud de adopción fue aprobada!"
        if approved
        else "Estado de tu solicitud de adopción"
    )

    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]

    text_content = (
        f"Hola {user.username},\n\n"
        f"Tu solicitud para adoptar a {adoption.pet.name} "
        f"{'ha sido aprobada 🎉' if approved else 'no fue aprobada en esta ocasión.'}"
    )

    message = (
        f"""
        ¡Felicidades! 🎉<br><br>
        Tu solicitud para adoptar a <strong>{adoption.pet.name}</strong>
        fue aprobada.<br><br>
        Pronto nos pondremos en contacto contigo para los siguientes pasos.
        """
        if approved
        else
        """
        Gracias por tu interés en la adopción.<br><br>
        En esta ocasión tu solicitud no fue aprobada, pero te animamos
        a seguir explorando otras mascotas que buscan un hogar.
        """
    )

    button = (
        """
        <a href="https://saavedra-pet-adoption.desarrollo-software.xyz"
           style="background-color: #16a34a; color: #ffffff;
                  padding: 12px 24px; text-decoration: none;
                  border-radius: 6px; font-weight: bold;">
          Ver siguientes pasos 🐾
        </a>
        """
        if approved
        else
        """
        <a href="https://saavedra-pet-adoption.desarrollo-software.xyz"
           style="background-color: #2563eb; color: #ffffff;
                  padding: 12px 24px; text-decoration: none;
                  border-radius: 6px; font-weight: bold;">
          Ver más mascotas 🐶
        </a>
        """
    )

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #f9fafb; padding: 20px;">
        <table width="100%" cellpadding="0" cellspacing="0">
          <tr>
            <td align="center">
              <table width="600" style="background: #ffffff; border-radius: 8px; padding: 30px;">

                <tr>
                  <td align="center" style="font-size: 28px; font-weight: bold; color: #111827;">
                    🐾 Puppy Family
                  </td>
                </tr>

                <tr><td height="20"></td></tr>

                <tr>
                  <td style="font-size: 16px; color: #374151;">
                    Hola <strong>{user.username}</strong>,
                  </td>
                </tr>

                <tr><td height="15"></td></tr>

                <tr>
                  <td style="font-size: 16px; color: #374151;">
                    {message}
                  </td>
                </tr>

                <tr><td height="25"></td></tr>

                <tr>
                  <td align="center">
                    {button}
                  </td>
                </tr>

                <tr><td height="30"></td></tr>

                <tr>
                  <td style="font-size: 14px; color: #9ca3af;">
                    — Equipo Puppy Family 🐶🐱
                  </td>
                </tr>

              </table>
            </td>
          </tr>
        </table>
      </body>
    </html>
    """

    try:
        email = EmailMultiAlternatives(subject, text_content, from_email, to)
        email.attach_alternative(html_content, "text/html")
        email.send()
    except Exception as e:
        logger.error(
            f"Error enviando correo RESULT (AdoptionRequest {adoption.id}): {e}"
        )