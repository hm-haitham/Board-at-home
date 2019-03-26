from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$',views.home),
    url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    url('register/', views.register, name = "register"),
    url('search/', views.search, name = "search"),
    url(r'^profile/$',views.profile, name ="profile")
]
    #url(r'^login/$', loginView, {{'template_name':'accounts/login.html'}})