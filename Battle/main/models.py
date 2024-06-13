"""
Файл для работы с моделями
"""

from django.db import models


class Enemy(models.Model):
    name = models.CharField(max_length=100)
    image_enemy = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)

    damage = models.IntegerField()
    min_damage = models.IntegerField()
    
    defeat = models.IntegerField()
    min_defeat = models.IntegerField()
    
    fases = models.IntegerField()
    hp = models.IntegerField()
    min_enemy_hp = models.IntegerField()
    max_enemy_hp = models.IntegerField()
    
    lvl = models.IntegerField()
    money = models.IntegerField()
    min_money = models.IntegerField()
    exp = models.IntegerField()
    min_exp = models.IntegerField()

    hero_defeat_debaf = models.IntegerField()
    hero_damage_debaf = models.IntegerField()


class Users(models.Model):
    """Установка полей для модели пользователей"""
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f'\n{self.login}\n{self.password}'
    

class Frases(models.Model):
    type = models.CharField(max_length=100)
    frase_text = models.TextField()
    enemy_hero = models.ForeignKey(Enemy, on_delete=models.CASCADE, blank=True, null=True)

     
class Heroes(models.Model):
    image_hero = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    damage = models.IntegerField()
    defeat = models.IntegerField()
    fases = models.IntegerField()
    bottles = models.IntegerField()
    bottle_hp = models.IntegerField()
    hp = models.IntegerField()
    max_hp = models.IntegerField()
    lvl = models.IntegerField()
    lvl_points = models.IntegerField()
    exp = models.IntegerField()
    exp_to_next_lvl = models.IntegerField()
    enemy = models.ForeignKey(Enemy, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class image_auth(models.Model):
    auth_image = models.CharField(max_length=100)
