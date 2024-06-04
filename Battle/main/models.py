"""
Файл для работы с моделями
"""

from django.db import models

class Recipes(models.Model):
    """Установка полей для модели рецептов"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ingredients = models.TextField()

    def __str__(self):
        return f'\n{self.name}:\n{self.description}\n{self.cooking_steps}\n{self.cooking_time}\
            \n{self.author}\n{self.ingredients}\n'


class Categories(models.Model):
    """Установка полей для модели категории"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'\n{self.name}\n'


class RecipesCategories(models.Model):
    """Установка полей для модели рецептов и категорий"""
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'\n{self.recipes.name}:\n{self.category.name}\n'