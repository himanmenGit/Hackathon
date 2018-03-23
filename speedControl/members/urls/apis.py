from django.urls import path

from ..views.apis import FacebookLogin

urlpatterns = [
    path('login/', FacebookLogin.as_view()),
]
