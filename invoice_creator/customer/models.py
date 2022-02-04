from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _  # for support multi language


class Customer(models.Model):
    """
    Model of customer that store information about customer
    """
    first_name = models.CharField(_('Firstname'), max_length=256)
    last_name = models.CharField(_('Lastname'), max_length=256)
    company = models.CharField(_('Company'), max_length=256)
    phone_number = models.CharField(_('Phone number'), max_length=32)
    email = models.EmailField(_('Email'), null=True, blank=True)
    mobile_number = models.CharField(
        _('Mobile number'),
        max_length=11,
        validators=[
            RegexValidator(r'09\d{9}'),  # validate phone number by regex
        ]
    )
    address = models.CharField(_('Address'), max_length=2048)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        """

        """
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        ordering = (
            'last_name',
            'first_name',
        )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        """
        Return full name of customer base on fist and last name
        """
        return f'{self.first_name} {self.last_name}'
