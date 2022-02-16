"""
Urls of invoice section must be define here
"""

from django.urls import path

from invoice import views

app_name = 'invoice'
urlpatterns = [
    path('<int:id>/', views.ViewInvoice.as_view(), name='view_invoice'),
    path('preview/<int:id>/', views.PrintPreviewInvoice.as_view(), name='print_preview'),
    path('get/<int:id>/', views.GetInvoice.as_view(), name='get_invoice'),
    path('send/<int:id>/', views.SendInvoice.as_view(), name='send_invoice')
]
