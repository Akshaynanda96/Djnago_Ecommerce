from django.conf import settings
from django.core.mail import send_mail

def send_active_account_email(email, email_token, first_name):
    subject = f'Hi, {first_name} this is a verification email'
    message = f'This is a verification link. Please click here to verify your account: http://127.0.0.1:8000/accounts/activate/{email_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    
    send_mail(subject, message, email_from, recipient_list)