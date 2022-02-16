from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_jalali.db.models import jDateTimeField


class WkhtmltopdfLog(models.Model):
    invoice = models.ForeignKey(
        'invoice.Invoice',
        on_delete=models.CASCADE,
        verbose_name=_('Invoice'),
        related_name='invoice_wkhtmltopdf_log'
    )
    log = models.TextField()
    time = jDateTimeField(_('Time'))
