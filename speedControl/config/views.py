from django.conf import settings
from django.shortcuts import render, redirect

from utils.sms import SMS


def index(request):
    return render(request, 'index.html')


prev_time = 0


def send_sms_view(request):
    global prev_time

    if request.method == 'POST':

        import datetime

        now_time = datetime.datetime.now()

        if now_time.timestamp() > prev_time:
            prev_time = now_time.timestamp() + (30 * 60 * 60)

            import random
            # 사용할때 이렇게 사용하면 됨.
            send_message = ['빠름 빠름 빠름', '쉬는 시간 입니다', '저는 아무것도 모르겠습니다']
            sms = SMS(to_number=settings.LHY_NUMBER, text=random.choice(send_message))

            sms.send_sms()
        next_path = request.POST.get('next-path')
        return redirect(next_path)

    return redirect('index')
