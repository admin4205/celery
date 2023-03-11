# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_greeting_email

def send_email(request):
    email = request.POST.get('email')

    # Call the Celery task to send the email asynchronously
    send_greeting_email.delay(email)

    return HttpResponse('Email sent successfully')
