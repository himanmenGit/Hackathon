from django.urls import path, re_path

from chatting.views import index, send_sms_view, room, chat

urlpatterns = [
    path('', index, name='index'),

    path('chat/', chat, name='chat-index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),

    path('send-sms/', send_sms_view, name='send-sms')
]
