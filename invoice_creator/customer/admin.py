from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from customer import models

admin.site.unregister(Group)


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Create functionality on customer model in admin panel
    """
    search_fields = (
        'first_name',
        'last_name',
        'company',
        'phone_number',
        'email',
        'mobile_number',
    )

    list_display = (
        'full_name',
        'report'
    )

    def report(self, obj):
        link_title = _('Report')
        link = reverse('customer:user_report', kwargs={'id': obj.id})
        return format_html(f'<a href="{link}" target="_blank">{link_title}</a>')

    report.allow_tags = True
    report.short_description = _('Report')
