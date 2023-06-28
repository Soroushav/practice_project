from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

import config.settings


def create_user_sent_email(username, email):
    context = {
        'username': username,
    }
    email_subject = 'Welcome to our community'
    email_body = render_to_string('account/email_create.txt', context=context)
    email_to = EmailMessage(subject=email_subject, body=email_body, to=[email,], from_email=config.settings.DEFAULT_FROM_EMAIL)
    return email_to.send(fail_silently=False)
