import random
from math import ceil

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_jalali.db.models import jDateTimeField

from notifications import KavenegarSMS, Email


def id_generator():
    return random.randint(100000, 1000000)


class InvoiceTemplate(models.Model):
    """
    If you want change style of invoice you can design it and upload to invoice template
    This model implemented for store new templates
    """
    name = models.CharField(unique=True, max_length=256)
    template = models.FileField(upload_to='invoice')

    class Meta:
        verbose_name = _('Invoice template')
        verbose_name_plural = _('Invoice templates')
        ordering = (
            'name',
        )


class CurrencyType(models.Model):
    name = models.CharField(_('Currency type'), max_length=32)

    class Meta:
        verbose_name = _('Currency type')
        verbose_name_plural = _('Currency types')
        ordering = (
            'name',
        )

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """
    This model keeps invoice
    """
    id = models.PositiveBigIntegerField(_('ID'), primary_key=True, default=id_generator)
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        verbose_name=_('Company'),
        null=True,
        blank=True
    )
    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.CASCADE,
        related_name='customer_invoice',
        verbose_name=_('Customer')
    )
    invoice_number = models.PositiveIntegerField(_('Invoice number'), null=True, blank=True)
    date = jDateTimeField(_('Date'))
    template = models.ForeignKey(
        InvoiceTemplate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_('Invoice template')
    )
    currency = models.ForeignKey(
        CurrencyType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Currency')
    )
    discount = models.FloatField(_('Discount'), default=0)
    discount_type = models.BooleanField(
        _('Discount type'),
        default=False,
        choices=(
            (True, _('Percent')),
            (False, _('Fix')),
        )
    )
    tax = models.FloatField(_('Tax'), default=0)
    tax_type = models.BooleanField(
        _('Tax type'),
        default=False,
        choices=(
            (True, _('Percent')),
            (False, _('Fix')),
        )
    )
    description = models.CharField(_('Description'), max_length=2048, null=True, blank=True)
    paid_time = jDateTimeField(_('Paid time'), null=True, blank=True)
    send_invoice_time = jDateTimeField(_('Send invoice time'), null=True, blank=True)

    class Meta:
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')
        ordering = (
            '-date',
            '-paid_time'
        )

    @property
    def total_fields(self):
        """
        Calculate total without discount and tax
        """
        return sum([i.sub_total for i in self.invoicefields_set.all()])

    @property
    def total_discount(self):
        """
        Calculate discount
        """
        total = self.total_fields
        if self.discount_type:
            discount = total * self.discount / 100
        else:
            discount = self.discount
        return ceil(discount)

    @property
    def total_tax(self):
        """
        Calculate tax
        """
        total = self.total_fields
        if self.tax_type:
            discount = total * self.tax / 100
        else:
            discount = self.tax
        return ceil(discount)

    @property
    def total(self):
        """
        Calculate total value of invoice
        """
        return self.total_fields - self.total_discount + self.total_tax

    @classmethod
    def get_invoice(cls, id):
        """
        Return invoice by ID
        """
        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    def send(self, request):
        """
        Send invoice by Email and SMS
        """
        lnk = request.build_absolute_uri(reverse('invoice:view_invoice', kwargs={'id': self.id}))
        if self.customer.email is not None:
            link = f'<a href="{lnk}">????????????</a>'
            Email.send_email(
                '????????????',
                f'???????? ???????????? ???????????? ?????? ???????? ???????? ????????: {link}',
                self.customer.email
            )
        if self.customer.mobile_number is not None:
            KavenegarSMS().send(
                self.customer.mobile_number,
                f'????????????:\n{lnk}'
            )
        self.send_invoice_time = timezone.now()
        self.save()

    @classmethod
    def get_customers_invoice(cls, customer, paid=None):
        """
        Return all invoices of the specific customer
        """
        if paid is None:
            return cls.objects.filter(customer=customer)
        elif paid:
            return cls.objects.filter(customer=customer, paid_time__isnull=False)
        else:
            return cls.objects.filter(customer=customer, paid_time__isnull=True)


class InvoiceFields(models.Model):
    """
    Keep fields of invoice
    """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=256)
    count = models.PositiveIntegerField(_('Count'), default=1)
    type = models.CharField(_('Type'), max_length=256, null=True, blank=True)
    cost = models.PositiveBigIntegerField(_('Price'), default=0)

    class Meta:
        verbose_name = _('Invoice field')
        verbose_name_plural = _('Invoice fields')
        ordering = (
            'invoice',
            'title'
        )

    def __str__(self):
        return self.title

    @property
    def sub_total(self):
        """
        Calculate total of a invoice row
        """
        return self.count * self.cost
