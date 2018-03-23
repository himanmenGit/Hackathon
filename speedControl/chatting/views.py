from django.shortcuts import render, redirect

from django.utils.safestring import mark_safe
import json

from utils.sms import SMS


def index(request):
    return render(request, 'index.html')


def chat(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    print(room_name)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def send_sms_view(request):
    import random

    # 사용할때 이렇게 사용하면 됨.
    send_message = ['빠름 빠름 빠름', '쉬는 쉬간 입니다', '저는 아무것도 모르겠습니다']
    sms = SMS(to_number='01051420203', text=random.choice(send_message))

    sms.send_sms()
    return redirect('index')
