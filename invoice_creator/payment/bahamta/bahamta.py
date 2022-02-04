from requests import get

from invoice_creator import settings

API_KEY = getattr(settings, 'BAHAMTA_API_KEY')
CALL_BACK = getattr(settings, 'BAHAMTA_CALL_BACK')


class Bahamta:
    create_url = 'https://webpay.bahamta.com/api/create_request'
    confirm_url = 'https://webpay.bahamta.com/api/confirm_payment'

    def __init__(self):
        self.api_key = API_KEY
        self.call_back = CALL_BACK

    def create(self, amount_ir, reference, currency='Rial', mobile=None):
        try:
            res = get(
                Bahamta.create_url,
                params={
                    'api_key': self.api_key,
                    'amount_irr': amount_ir if currency == 'Rial' else amount_ir * 10,
                    'reference': reference,
                    'callback_url': self.call_back,
                    'payer_mobile': mobile
                }
            )
            if res.ok:
                return res.json().get('ok'), res.json()
            raise Exception
        except:
            return None

    def confirm(self, amount_ir, reference, currency='Rial'):
        try:
            res = get(
                Bahamta.confirm_url,
                params={
                    'api_key': self.api_key,
                    'amount_irr': amount_ir if currency == 'Rial' else amount_ir * 10,
                    'reference': reference,
                    'callback_url': self.call_back
                }
            )
            if res.ok:
                return res.json().get('ok') and res.json().get('result').get('state') == 'paid', res.json()
            raise Exception
        except:
            return None
