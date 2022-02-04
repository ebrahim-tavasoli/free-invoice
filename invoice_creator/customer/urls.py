"""
Urls of customer application define here
"""

from django.urls import path

from customer import views

app_name = 'customer'
urlpatterns = [
    path('report/<int:id>/', views.UserReport.as_view(), name='user_report'),

]
