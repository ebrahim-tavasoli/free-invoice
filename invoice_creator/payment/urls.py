from django.urls import path

from payment import views

app_name = 'payment'
urlpatterns = [
    path('callback/', views.CallBackPayment.as_view(), name='payment_callback')
]
