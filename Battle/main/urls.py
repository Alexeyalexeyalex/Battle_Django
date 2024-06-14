"""
Установка путей и привязка представлений
"""
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.battle, name='battle'),
    path('start/<str:text>/', views.start, name='start'),
    path('battle/', views.battle, name='battle'),
    path('make_damage/', views.make_damage, name='make_damage'),
    path('leave/', views.leave, name='leave'),
    path('healing/', views.healing, name='healing'),
    path('up_damage/', views.up_damage, name='up_damage'),
    path('up_defeat/', views.up_defeat, name='up_defeat'),
    path('up_bottle_hp/', views.up_bottle_hp, name='up_bottle_hp'),
    path('up_max_hp/', views.up_max_hp, name='up_max_hp'),

    path('buy_bottle/', views.buy_bottle, name='buy_bottle'),
    path('buy_scroll/', views.buy_scroll, name='buy_scroll'),
    path('buy_luck_bottle/', views.buy_luck_bottle, name='buy_luck_bottle'),
    path('buy_death_bottle/', views.buy_death_bottle, name='buy_death_bottle'),

    path('buy_default/', views.buy_default, name='buy_default'),
    path('buy_patrik/', views.buy_patrik, name='buy_patrik'),
    path('buy_zombi/', views.buy_zombi, name='buy_zombi'),
    path('buy_mumi/', views.buy_mumi, name='buy_mumi'),



    path('about/', views.about, name='about'),
    path('leaders/', views.leaders, name='leaders'),
    path('login/', views.login, name='login'),
    path('shop/', views.shop, name='shop'),
    
]
