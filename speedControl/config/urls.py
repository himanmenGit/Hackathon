from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config.views import index, send_sms_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('send-sms/', send_sms_view, name='send-sms'),

    path('chat/', include('chatting.urls')),

    path('members/', include('members.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
