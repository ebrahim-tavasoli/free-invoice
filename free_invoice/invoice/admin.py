from django.contrib import admin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

from invoice import models


@admin.register(models.CurrencyType)
class CurrencyType(admin.ModelAdmin):
    pass


class InvoiceFieldsInline(admin.TabularInline):
    model = models.InvoiceFields


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """
    Create functionality of invoice model in admin panel
    """
    inlines = [
        InvoiceFieldsInline,
    ]
    list_display = (
        'id',
        'customer',
        'invoice_number',
        'date',
        'paid_time',
        'send',
        'download_link',
    )
    search_fields = (
        'id',
        'customer',
        'invoice_number',
    )
    list_filter = (
        'paid_time',
    )

    def send(self, obj):
        """
        Send invoice by sms
        """
        link_title = _('Send')
        link = reverse('invoice:send_invoice', kwargs={'id': obj.id})
        return format_html(f'<a href="{link}">{link_title}</a>')

    send.allow_tags = True
    send.short_description = _('Send')

    def download_link(self, obj):
        """
        Make pdf of invoice
        """
        link_title = _('Download')
        link = reverse('invoice:print_preview', kwargs={'id': obj.id})
        return format_html(f'<a href="{link}">{link_title}</a>')

    download_link.allow_tags = True
    download_link.short_description = _('Download')


admin.site.register(models.InvoiceTemplate)  # Add invoice template functionality in admin panel
