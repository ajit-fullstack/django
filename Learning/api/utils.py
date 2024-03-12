from django.core.mail import send_mail
from django.conf import settings

def send_to_email():
    subject = "This email is from django server"
    message = "This is a test mail "
    form_email = settings.EMAIL_HOST_USER
    print(settings.EMAIL_HOST_USER, "settings.EMAIL_HOST_USER")
    recipient_list = ["anujsingh6779@gmail.com"]
    send_mail(subject, message, form_email, recipient_list)
    