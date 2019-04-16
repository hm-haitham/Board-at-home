from django.conf.urls import url
from . import views
from . import recommendations
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    url(r'^$',views.home),
    url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    url('register/', views.register, name = "register"),
    url('search/', views.search, name = "search"),
    url('about/', views.about, name = 'about'),
    url('nearby_players', views.find_nearby_players, name = "findnearby"),
    url('game_based_recommandations/', recommendations.game_based_recommandations, name="game_based_recommandations"),
    url(r'^random/$', views.get_random_game, name="random"),
    url(r'^profile/$',views.view_profile, name ="view_profile"),
    url(r'^profile/remove_wishlist/(?P<game_id>[0-9]+)/$',views.remove_from_wishlist, name ="remove_from_wishlist"),
    url(r'^profile/remove_ownedlist/(?P<game_id>[0-9]+)/$',views.remove_from_ownedlist, name ="remove_from_ownedlist"),
    url(r'^profile/edit/$',views.edit_profile, name ="edit_profile"),
]
    #url(r'^login/$', loginView, {{'template_name':'accounts/login.html'}})
