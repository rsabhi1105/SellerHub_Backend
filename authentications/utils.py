from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_email(user_email, activation_link):
    subject = "Activate your account on" + settings.SITE_NAME
    from_email = settings.EMAIL_HOST_USER
    to = [user_email]

    # load html template
    html_content = render_to_string("activation_email.html", {"activation_link": activation_link})

    # creat email body with plane text
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()


def reset_pass_link(user_email, reset_link):
    subject = "reset your password on" + settings.SITE_NAME
    from_email = settings.EMAIL_HOST_USER
    to = [user_email]

    # load html template
    html_content = render_to_string("reset_pass.html", {"reset_pass": reset_link})

    # creat email body with plane text
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
