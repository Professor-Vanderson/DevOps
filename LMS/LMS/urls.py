from django.conf.urls import url
from django.contrib import admin
from escola.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
]
