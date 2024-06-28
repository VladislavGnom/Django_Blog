from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout_then_login/', auth_views.logout_then_login, name='logout_then_login'),
    path('register/', views.register, name='register')
]

