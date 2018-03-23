from django.urls import path, include

urlpatterns = [
    path('', include('members.urls.apis')),
]
