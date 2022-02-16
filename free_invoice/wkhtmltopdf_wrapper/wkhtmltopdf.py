import tempfile
from subprocess import Popen, PIPE

from invoice.models import Invoice
from wkhtmltopdf_wrapper import models


class Wkhtmlto:
    program = ''

    def __init__(self, invoice: Invoice, content=None, html_content=False, size='A4', orientation='Portrait'):
        self.invoice = invoice
        if html_content:
            self.tmp_html = tempfile.NamedTemporaryFile('wt')
            self.tmp_html.write(content)
            self.tmp_html.seek(0)
            self.tmp_pdf = tempfile.NamedTemporaryFile('rb')
            self.tmp_pdf.seek(0)
        p = Popen([Wkhtmlto.program, '-s', size, '-O', orientation, self.tmp_html.name, self.get_path()],
                  stdout=PIPE, stderr=PIPE, shell=True)
        if p.wait() != 0:
            output, error = p.communicate()
            models.WkhtmltopdfLog.objects.create(invoice=invoice, log=error)

    def get_path(self):
        return self.tmp_pdf.name

    def get_file_binary(self):
        self.tmp_pdf.seek(0)
        return self.tmp_pdf.read()

    def remove_files(self):
        self.tmp_html.close()
        self.tmp_pdf.close()

    def __del__(self):
        try:
            self.remove_files()
        except:
            pass


class Wkhtmltopdf(Wkhtmlto):
    program = 'wkhtmltopdf'


class Wkhtmltoimage(Wkhtmlto):
    program = 'wkhtmltoimage'
