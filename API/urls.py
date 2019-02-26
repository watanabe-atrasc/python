from django.urls import path
from . import views

urlpatterns = [
    path('getInfo', views.SyainSelect, name='getInfo'),
    path('login',views.Login, name='login')
]