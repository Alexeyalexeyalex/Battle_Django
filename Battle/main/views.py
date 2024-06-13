"""
Файл представлений
"""
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from random import choice, randint
from main.models import Enemy, Heroes, Users

global player_id, enemy_id
player_id=''
enemy_id=''


def make_damage(request):
    global enemy_id, player_id
    my_enemy = Enemy.objects.filter(id=enemy_id).first() #without first() the result is ObjectSet not Object
    hero = Heroes.objects.get(user=player_id)

    if hero.damage > my_enemy.defeat:
        my_enemy.hp-=hero.damage-my_enemy.defeat

    if my_enemy.hp < 1:
        if my_enemy.fases > 1:
            my_enemy.fases-=1
            my_enemy.hp=my_enemy.max_enemy_hp
        else:
            hero.exp += my_enemy.exp
            hero.enemy=None

            my_enemy.damage = my_enemy.min_damage
            my_enemy.defeat = my_enemy.min_defeat
            my_enemy.hp = my_enemy.min_enemy_hp
            my_enemy.money = my_enemy.min_money
            my_enemy.exp = my_enemy.min_exp
            my_enemy.lvl = 1

            if hero.exp_to_next_lvl <= hero.exp:
                hero.lvl += 1 
                hero.lvl_points += 1
                exp = hero.exp - hero.exp_to_next_lvl
                hero.exp = exp
                hero.exp_to_next_lvl = hero.exp_to_next_lvl*10/2
            hero.save()
            my_enemy.save()
            return redirect ("start", text='Вы убили врага!')
    else:
        if my_enemy.damage > hero.defeat:
            hero.hp-=my_enemy.damage-hero.defeat
            if hero.hp<1:
                leave(request)
                hero.delete()
                return redirect ("start", text='Вы погибли(')


        
    hero.save()
    my_enemy.save() # to save object to the db
    return redirect ("battle")

def healing(request):
    global enemy_id, player_id
    hero = Heroes.objects.get(user=player_id)
    if hero.hp < hero.max_hp and hero.bottles > 0:
        hero.hp += hero.bottle_hp
        if hero.hp > hero.max_hp:
            hero.hp = hero.max_hp
        hero.bottles -= 1
        hero.save()
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

def money_up(person):
    person.money+=randint(1,50)

def enemy_lvl_up(person):
    lvl_up(person)
    exp_up(person)
    money_up(person)
    choice((hp_up, defeat_up, damage_up))(person)


def start(request, text):
    start = {
        'text':text,
        
    }
    return render(request, 'main/start.html', {'start':start})


def battle(request):
    """Отображение """
    global player_id, enemy_id
    
    if not  player_id:
        return render(request, 'main/not_login.html')
    try:
        hero = Heroes.objects.get(user=player_id)
    except:
        hero = Heroes(
                image_hero = "main/images/spounch1.png",
                image_back = "main/images/spounch_back.jpg",
                damage = 1,
                defeat = 0,
                fases = 1,
                bottles = 1,
                bottle_hp = 1,
                hp = 3,
                max_hp = 3,
                lvl = 1,
                lvl_points = 0,
                exp = 0,
                exp_to_next_lvl = 10,
                user = Users.objects.get(id=player_id),
                )

        hero.save()
    enemy = hero.enemy
    if not hero.enemy:
        enemy = choice(Enemy.objects.all())
        hero.enemy=enemy
        hero.save()
    enemy_id = enemy.id

    hearts_enemy = list()
    hearts = enemy.hp
    for i in range(5):
        if hearts>0:
            hearts_enemy.append(1)
            hearts-=1
        else:
            hearts_enemy.append(0)

    hearts_hero = list()
    hearts = hero.hp
    for i in range(5):
        if hearts>0:
            hearts_hero.append(1)
            hearts-=1
        else:
            hearts_hero.append(0)
    hearts_hero = hearts_hero[::-1]
    battle = {
        
        'image_hero':hero.image_hero,
        'image_hero_back':hero.image_back,
        'damage_hero':hero.damage,
        'defeat_hero':hero.defeat,
        'fases_hero':hero.fases,
        'bottles_hero':hero.bottles,
        'hp_hero':hero.hp,
        'lvl_range':enemy.lvl-hero.lvl,
        'lvl_points':hero.lvl_points,
        'hearts_hero':hearts_hero,

        'name_enemy':enemy.name,
        'image_enemy':enemy.image_enemy,
        'image_back_enemy':enemy.image_back,
        'damage_enemy':enemy.damage,
        'defeat_enemy':enemy.defeat,
        'fases_enemy':enemy.fases,
        'hp_enemy':enemy.hp,
        'lvl_enemy':enemy.lvl,
        'money_enemy':enemy.money,
        'hearts_enemy':hearts_enemy,
    
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