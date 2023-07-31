from django.core.mail import send_mail
from django.conf import settings
import random
import string

def generate_verification_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

def send_verification_email(user, email_verification):
    token = email_verification.token
    verification_url = f"http://127.0.0.1:8000/verify_email/?token={token}"

    subject = "이메일 인증 메일"
    message = f"아래 링크를 클릭하여 이메일을 인증하세요: {verification_url}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)