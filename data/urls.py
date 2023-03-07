from django.urls import path
from . import views

app_name='data'

urlpatterns = [
    path('index/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
]