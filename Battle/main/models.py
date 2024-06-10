"""
Файл для работы с моделями
"""

from django.db import models



class Users(models.Model):
    """Установка полей для модели пользователей"""
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    lvl = models.IntegerField()

    def __str__(self):
        return f'\n{self.login}\n{self.password}'

class Enemy(models.Model):
    name = models.CharField(max_length=100)
    image_enemy = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    damage = models.IntegerField()
    defeat = models.IntegerField()
    fases = models.IntegerField()
    hp = models.IntegerField()
    lvl = models.IntegerField()
    money = models.IntegerField()


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
    hp = models.IntegerField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)



