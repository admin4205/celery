from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail

@shared_task(name='send_greeting_email')
def send_greeting_email(email):
    subject = 'Welcome to My App!'
    message = 'Thank you for signing up for My App. We hope you enjoy using our service!'
    from_email = 'rochakbhattarai11@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
