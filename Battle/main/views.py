"""
Файл представлений
"""
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from random import choice, randint
from main.models import Enemy, Heroes
global player_id, enemy_id
player_id=''
enemy_id=''

def make_damage(request):
    global enemy_id
    print(enemy_id)
    my_enemy = Enemy.objects.filter(id=enemy_id).first() #without first() the result is ObjectSet not Object
    my_enemy.hp-=1
    my_enemy.save() # to save object to the db
    return redirect ("battle")

def leave(request):
    global player_id, enemy_id
    my_enemy = Enemy.objects.filter(id=enemy_id).first() #without first() the result is ObjectSet not Object
    enemy_lvl_up(my_enemy)
    my_enemy.save() # to save object to the db

    hero = Heroes.objects.get(user=player_id)
    hero.enemy=None
    hero.save()
    return redirect ("battle")
    




def lvl_up(person, lvl_to_up=1):
    person.lvl+=lvl_to_up

def hp_up(person, hp_to_up=1):
    if  person.hp < person.max_enemy_hp:
        person.hp = person.max_enemy_hp
    person.hp+=hp_to_up
    person.max_enemy_hp+=hp_to_up

def defeat_up(person, defeat_to_up=1):
    person.defeat+=defeat_to_up

def damage_up(person, damage_to_up=1):
    person.damage+=damage_to_up

def exp_up(person):
    person.exp+=randint(1,50)

def enemy_lvl_up(person):
    lvl_up(person)
    exp_up(person)
    choice((hp_up, defeat_up, damage_up))(person)



def battle(request):
    """Отображение """
    global player_id, enemy_id
    
    if not  player_id:
        return render(request, 'main/not_login.html')
    hero = Heroes.objects.get(user=player_id)
    
    enemy = hero.enemy
    if not hero.enemy:
        enemy = choice(Enemy.objects.all())
        hero.enemy=enemy
        hero.save()
    enemy_id = enemy.id

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


def shop(request):
    """Отображение """
    return render(request, 'main/shop.html')

def about(request):
    """Отображение """
    return render(request, 'main/about.html')

def leaders(request):
    """Отображение """
    return render(request, 'main/leaders.html')

def login(request):
    """Отображение """
    global player_id
    player_id = 1
    return render(request, 'main/login.html')