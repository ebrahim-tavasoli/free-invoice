from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class InvoiceConfig(AppConfig):
    name = 'invoice'
    verbose_name = _('Invoice')
