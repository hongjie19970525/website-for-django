
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from mainsite.views import homepage,showpost

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',homepage),
    url(r'^post/(\w+)$',showpost),
]
