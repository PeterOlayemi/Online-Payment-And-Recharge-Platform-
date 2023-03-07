from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='account'

urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('signin/', auth_views.LoginView.as_view(), name='login'),
    path('signout/', views.signout, name = 'logout'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('user/welcome/', views.welcome, name = 'welcome'),
    path('terms_of_service/', views.term, name = 'term'),
    path('privacy_policy/', views.privacy, name = 'privacy'),
    path('add_info/', views.myuser, name = 'myuser'),
    path('my_profile/', views.profile, name='profile'),
]
