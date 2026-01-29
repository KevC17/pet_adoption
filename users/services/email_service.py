from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_welcome_email(user):
    subject = '🐾 Bienvenido a Puppy Family'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [user.email]

    text_content = (
        f'Hola {user.username},\n\n'
        'Bienvenido a Puppy Family.\n'
        'Gracias por unirte a nuestra comunidad.'
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
                    ¡Gracias por unirte a <strong>Puppy Family</strong>!<br><br>
                    Ahora formas parte de una comunidad que cree que cada mascota
                    merece un hogar lleno de amor.
                  </td>
                </tr>

                <tr><td height="20"></td></tr>

                <tr>
                  <td style="font-size: 16px; color: #374151;">
                    <strong>Desde ahora puedes:</strong>
                    <ul>
                      <li>Explorar mascotas disponibles para adopción</li>
                      <li>Enviar solicitudes fácilmente</li>
                      <li>Dar seguimiento a todo el proceso</li>
                    </ul>
                  </td>
                </tr>

                <tr><td height="20"></td></tr>

                <tr>
                  <td align="center">
                    <a href="https://puppyfamily.com"
                       style="background-color: #2563eb; color: #ffffff;
                              padding: 12px 24px; text-decoration: none;
                              border-radius: 6px; font-weight: bold;">
                      Explorar mascotas 🐾
                    </a>
                  </td>
                </tr>

                <tr><td height="30"></td></tr>

                <tr>
                  <td style="font-size: 14px; color: #6b7280;">
                    Cada adopción cambia una vida ❤️<br>
                    Gracias por ser parte del cambio.
                  </td>
                </tr>

                <tr><td height="15"></td></tr>

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

    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
