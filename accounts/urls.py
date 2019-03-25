from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^$',views.home),
    url('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="login"),
    url('register/', views.register, name = "register")
]
    #url(r'^login/$', loginView, {{'template_name':'accounts/login.html'}})
