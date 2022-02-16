from kavenegar import *
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from free_invoice import settings

SENDER = settings.KAVENEGAR_SENDER

class Email:
    @staticmethod
    def send_email(title, body, email):
        EmailMessage(
            subject=title,
            body=body,
            from_email=settings.DEFAULT_EMAIL,
            to=[email, ],
        ).send()


class KavenegarSMS:

    def __init__(self):
        self.api = KavenegarAPI(settings.KAVENEGAR_API_KEY)

    def send(self, receptor, message):
        params = {
            'sender': SENDER,
            'receptor': receptor,
            'message': message
        }
        self.api.sms_send(params)
