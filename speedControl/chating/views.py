from django.shortcuts import render, redirect

from utils.sms import SMS


def index(request):
    return render(request, 'index.html')


def send_sms_view(request):
    import random

    # 사용할때 이렇게 사용하면 됨.
    send_message = ['빠름 빠름 빠름', '쉬는 쉬간 입니다', '저는 아무것도 모르겠습니다']
    sms = SMS(to_number='01051420203', text=random.choice(send_message))

    sms.send_sms()
    return redirect('index')
