from django.db import models
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    logo = models.ImageField(_('Logo'), null=True, blank=True, upload_to='company/logo')
    sign = models.ImageField(_('Sign'), null=True, blank=True, upload_to='company/sign')

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Company')
        ordering = (
            'name',
        )

    def __str__(self):
        return self.name
