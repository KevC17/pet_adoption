from django.core.mail import send_mail
from django.conf import settings


def send_welcome_email(user):
    """
    Envía correo de bienvenida al usuario recién registrado
    """
    subject = 'Bienvenido a Pet Adoption 🐾'

    message = (
        f'Hola {user.username},\n\n'
        'Gracias por registrarte en Pet Adoption.\n\n'
        'Desde ahora puedes:\n'
        '• Buscar mascotas disponibles\n'
        '• Enviar solicitudes de adopción\n'
        '• Hacer seguimiento a tus solicitudes\n\n'
        'Tu ayuda cambia vidas 🐶🐱\n\n'
        '— Equipo Pet Adoption'
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
