from django.core.mail import send_mail
from django.conf import settings
import uuid

def send_password_mail(email,token):
    
    subject = 'Your Forgot Password Link'
    message = f'Hi,\n \n Click on the link to reset your password http://localhost:8000/change_pass/{token}/. \n Please wait for the approval.\n \n Regards \n \n Admin'
    from_email = settings.EMAIL_HOST_USER
    recipient_list =[email]
    send_mail(subject,message,from_email,recipient_list)
    return True