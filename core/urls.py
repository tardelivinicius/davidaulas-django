from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from core.router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include(router.urls))
]
