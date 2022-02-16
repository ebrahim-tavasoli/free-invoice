import io

from django.urls import reverse
from pdfkit import from_url as convert_to_pdf

from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.template.loader import render_to_string
from django.views import View
from django.shortcuts import get_object_or_404, render

from free_invoice import settings
from invoice import models
from payment.bahamta.bahamta import Bahamta
from payment import models as payment_models

BASE_DIR = settings.BASE_DIR


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
                invoice.customer.mobile_number
            )
            payment_obj.payment_url = payment_create_body.get('result', {}).get('payment_url', None)
            payment_obj.save()
        return render(
            request,
            'invoice/invoice.html',
            {'invoice': invoice, 'payment_url': payment_obj.payment_url}
        )


class PrintPreviewInvoice(View):
    def get(self, request, id=None):
        invoice = get_object_or_404(models.Invoice, id=id)
        return render(
            request,
            'invoice/invoice_template.html',
            {'invoice': invoice}
        )


class GetInvoice(View):
    """
    Return an invoice by id as PDF form.
    Support http get method only
    """

    def get(self, request, id=None):
        get_object_or_404(models.Invoice, id=id)
        x = request.build_absolute_uri(reverse('invoice:Print_preview', args=(id, )))
        pdf = convert_to_pdf(x, options={'orientation': 'Landscape'})
        return HttpResponse(
            pdf,
            content_type='application/pdf'
        )


class SendInvoice(View):
    """
    The view what send invoice
    """

    def get(self, request, id):
        invoice = get_object_or_404(models.Invoice, id=id)
        invoice.send(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
