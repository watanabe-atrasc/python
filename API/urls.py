from django.urls import path
from . import views

urlpatterns = [
    path('getInfo', views.GetInfo, name='getInfo'),
    path('login',views.Login, name='login'),
    path('record',views.Record, name='record')
]