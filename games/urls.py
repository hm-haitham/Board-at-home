from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<game_id>[0-9]+)/add_wishlist/$', views.add_to_wishlist, name="add_to_wishlist"),
    url(r'^(?P<game_id>[0-9]+)/add_owned/$', views.add_to_ownedlist, name="add_to_ownedlist"),
    url(r'^(?P<game_id>[0-9]+)/add_rating/(?P<score>[0-5]+)/$', views.add_rating, name="add_rating")
]

