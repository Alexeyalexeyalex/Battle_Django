"""
Файл для добавления моделей на страницу администратора
"""
from django.contrib import admin

from .models import Users, Frases, Enemy, Heroes

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """Структурирует информацию о смежной таблице рецептов и категорий"""
    list_display = ['login', 'password','lvl']

@admin.register(Frases)
class FrasesAdmin(admin.ModelAdmin):
    """Структурирует информацию о смежной таблице рецептов и категорий"""
    list_display = ['type', 'frase_text', 'enemy_hero']

@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    """Структурирует информацию о смежной таблице рецептов и категорий"""
    list_display = ['name', 'image_enemy', 'image_back', 'damage', 'defeat', 'fases', 'hp', 'lvl', 'money']

@admin.register(Heroes)
class HeroesAdmin(admin.ModelAdmin):
    """Структурирует информацию о смежной таблице рецептов и категорий"""
    list_display = ['image_hero', 'image_back', 'damage', 'defeat', 'fases', 'bottles', 'hp', 'user']
