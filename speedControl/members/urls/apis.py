from django.urls import path

from ..views.apis import FacebookLogin, FacebookUserGetInfo

urlpatterns = [
    path('info/', FacebookUserGetInfo.as_view()),
    path('login/', FacebookLogin.as_view()),
]
