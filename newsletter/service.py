from django.core import mail
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.utils.html import strip_tags

from ugrainfo.settings.base import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL,EMAIL_BACKEND
from post.models import PostPage


def send(email):
    subject = 'tt'
    data = dict()
    data['post'] = PostPage.objects.all()
    data['titles'] = PostPage.objects.values('title')
    data['url'] = PostPage.get_absolute_url
    template = get_template("data.html")
    html_text = template.render(data)
    plain_text = strip_tags(html_text)

    with mail.get_connection(backend=EMAIL_BACKEND, fail_silently=False) as connection:
        connection.open()  # Construct an email message that uses the connection
        send_mail(
            subject=subject,
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[email,],
            message=plain_text,
            html_message=html_text,
            connection=connection
        )
        # msg = EmailMessage(subject, message, text ,from_email, [email,], connection=connection)
        # msg.send(fail_silently=False)
        connection.close()

