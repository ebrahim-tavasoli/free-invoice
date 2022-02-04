from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views import View
from django.shortcuts import get_object_or_404, render

from weasyprint import HTML

from invoice import models
from payment.bahamta.bahamta import Bahamta
from payment import models as payment_models


class ViewInvoice(View):
    """
    Return an invoice by id as html form.
    Support http get method only
    """

    def get(self, request, id=None):
        invoice = get_object_or_404(models.Invoice, id=id)
        payment_obj, created = payment_models.Payment.objects.get_or_create(invoice=invoice)
        if created or payment_obj.payment_url is None:
            payment_create_status, payment_create_body = Bahamta().create(
                invoice.total,
                invoice.id,
                'Toman',
                invoice.customer.mobile_number
            )
            payment_obj.payment_url = payment_create_body.get('result', {}).get('payment_url', None)
            payment_obj.save()
        return render(request, 'invoice/invoice.html', {'invoice': invoice, 'payment_url': payment_obj.payment_url})


class GetInvoice(View):
    """
    Return an invoice by id as PDF form.
    Support http get method only
    """

    def get(self, request, id=None):
        if id is not None:
            invoice = get_object_or_404(models.Invoice, id=id)
            if invoice.template is not None:
                h = HTML(string=render_to_string(invoice.template, {'invoice': invoice}))
            else:
                h = HTML(string=render_to_string('invoice/invoice_template.html', {'invoice': invoice}))
            return HttpResponse(h.write_pdf(), content_type='application/pdf')
        return render(request, 'invoice/invoice.html', {})


class SendInvoice(View):
    """
    The view what send invoice
    """
    def get(self, request, id):
        invoice = get_object_or_404(models.Invoice, id=id)
        invoice.send(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
