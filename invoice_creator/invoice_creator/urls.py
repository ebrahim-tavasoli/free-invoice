"""invoice_creator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _


admin.site.site_header = _('Accounting')
admin.site.site_title = _('Accounting')

urlpatterns = i18n_patterns(
    path('', admin.site.urls),
    path('invoice/', include(('invoice.urls', 'invoice'), namespace='invoice'), name='invoice'),
    path('customer/', include(('customer.urls', 'customer'), namespace='customer'), name='customer'),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment'), name='payment')
)
