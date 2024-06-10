"""
Файл представлений
"""
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from random import choice
from main.models import Enemy, Heroes

def battle(request, user_id=1, method=''):
    """Отображение """

    if method == 1:
        my_enemy = Enemy.objects.filter(enemy_id=1)
        my_enemy.hp-=1
        print("asdasdasd")

    hero = Heroes.objects.get(user=user_id)
    enemy = choice(Enemy.objects.all())

    battle = {
        
        'image_hero':hero.image_hero,
        'image_hero_back':hero.image_back,
        'damage_hero':hero.damage,
        'defeat_hero':hero.defeat,
        'fases_hero':hero.fases,
        'bottles_hero':hero.bottles,
        'hp_hero':hero.hp,

        'name_enemy':enemy.name,
        'image_enemy':enemy.image_enemy,
        'image_back_enemy':enemy.image_back,
        'damage_enemy':enemy.damage,
        'defeat_enemy':enemy.defeat,
        'fases_enemy':enemy.fases,
        'hp_enemy':enemy.hp,
        'lvl_enemy':enemy.lvl,
        'money_enemy':enemy.money,
    
    }

    return render(request, 'main/battle.html', {'battle':battle})


def about(request):
    """Отображение """
    return render(request, 'main/about.html')

def leaders(request):
    """Отображение """
    return render(request, 'main/leaders.html')

def login(request):
    """Отображение """
    return render(request, 'main/login.html')