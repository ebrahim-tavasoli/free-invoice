from django.db import models
from django_jalali.db.models import jDateTimeField


class Payment(models.Model):
    invoice = models.OneToOneField('invoice.Invoice', on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.BooleanField('Payment status', default=False, blank=True)
    payment_number = models.CharField('Payment number', max_length=128, null=True, blank=True)
    payment_time = jDateTimeField('Payment time', null=True, blank=True)
    payment_gateway_response = models.JSONField('Payment gateway response', null=True, blank=True)
    insert_time = jDateTimeField('Insert time', auto_now_add=True)
    payment_url = models.URLField(max_length=2048, null=True)
