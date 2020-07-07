from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('home', views.HomeView.as_view(), name='home'),
    path('logout', views.logout_view, name='logout')
]
