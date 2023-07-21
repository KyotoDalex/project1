from ugrainfo.celery import app
from .service import send
from .models import SubscribedUsers
from django.core import mail
from django.core.mail import send_mail, EmailMessage
from ugrainfo.settings.base import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL,EMAIL_BACKEND

@app.task
def send_spam(email):
    send(email)


# @app.task
# def mail_scheduler():
#     template = get_template("mailing.html")
#     html_text = template.render()
#     for mails in SubscribedUsers.objects.all():
#         from_email = DEFAULT_FROM_EMAIL
#         subject = 'Новые публикации'
#         message = html_text
#         with mail.get_connection(backend=EMAIL_BACKEND, fail_silently=False) as connection:
#             connection.open()  # Construct an email message that uses the connection
#             msg = EmailMessage(subject, message, from_email, [mails.email, ], connection=connection)
#             msg.send(fail_silently=False)
#             connection.close()