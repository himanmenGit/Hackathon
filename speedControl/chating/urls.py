from django.urls import path, include

from chating.views import Chating

urlpatterns = [
    path('', Chating, name='chaing'),
]
