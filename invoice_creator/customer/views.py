from django.shortcuts import render, get_object_or_404
from django.views import View

from customer import models
from invoice import models as invoice_models


class UserReport(View):
    """
    Return a report about a user
    """

    def get(self, request, id):
        """
        Execute if come a http get request
        """
        customer = get_object_or_404(
            models.Customer,
            id=id
        )
        invoices = invoice_models.Invoice.get_customers_invoice(customer)
        return render(
            request,
            'customer/report.html',
            {
                'invoices_count': invoices.count(),
                'invoices_price': sum((i.total for i in invoices)),
                'unpaid_invoice_count': invoices.filter(paid_time__isnull=True).count(),
                'unpaid_invoice_price': sum((i.total for i in invoices.filter(paid_time__isnull=True)))
            }
        )
