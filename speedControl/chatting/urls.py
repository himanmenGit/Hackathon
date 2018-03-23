from django.urls import re_path

from chatting.views import room

urlpatterns = [
    # sudo apt-get install redis-server
    # 하고 redis-server 실행 해야 채팅 가능
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
