import requests
from django.conf import settings
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import redirect

User = get_user_model()

__all__ = (
    'login_view',
    'logout_view',
)


def login_view(request):
    code = request.GET.get('code')
    user = authenticate(request, code=code)
    print(user)
    if user is not None:
        login(request, user)
    return redirect('room', room_name='wps')


def logout_view(request):
    logout(request)
    return redirect('index')
