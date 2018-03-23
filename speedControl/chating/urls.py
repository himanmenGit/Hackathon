from django.urls import path

from chating.views import index, send_sms_view

urlpatterns = [
    path('', index, name='index'),
    path('send-sms/', send_sms_view, name='send-sms')
]
