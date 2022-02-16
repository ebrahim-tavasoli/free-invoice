from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views import View

from payment import models
from payment.bahamta.bahamta import Bahamta


class CallBackPayment(View):

    def get(self, request):
        if request.GET.get('state') == 'wait_for_confirm':
            try:
                obj = models.Payment.objects.get(
                    invoice_id=int(request.GET.get('reference'))
                )
                confirm = Bahamta().confirm(obj.invoice.total, obj.invoice.id, currency='Toman')
                if confirm[0] and obj.payment_time is None:
                    obj.payment_time = timezone.now()
                    obj.payment_status = True
                    obj.payment_number = confirm[1].get('result').get('pay_trace')
                    obj.payment_time = timezone.now()
                    obj.payment_gateway_response = confirm[1]
                    obj.invoice.paid_time = timezone.now()
                    obj.save()
                    obj.invoice.save()
                    return redirect('invoice:view_invoice', id=obj.invoice.id)
                raise models.Payment.DoesNotExist
            except models.Payment.DoesNotExist:
                pass
        return HttpResponse(
            'پرداخت انجام نشد. در صورت کم شدن پول از حساب '
            'شما حداکثر تا ۷۲ ساعت آینده به حساب شما برگشت داده خواهد شد.'
        )
