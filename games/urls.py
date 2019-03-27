from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name="detail")
]

