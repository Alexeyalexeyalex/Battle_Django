"""
Установка путей и привязка представлений
"""
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.battle, name='battle'),
    path('battle/', views.battle, name='battle'),
    path('make_damage/', views.make_damage, name='make_damage'),
    path('leave/', views.leave, name='leave'),
    path('healing/', views.healing, name='healing'),
    path('about/', views.about, name='about'),
    path('leaders/', views.leaders, name='leaders'),
    path('login/', views.login, name='login'),
    path('shop/', views.shop, name='shop'),
    
]
