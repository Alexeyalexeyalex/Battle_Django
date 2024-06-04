"""
Файл для работы с формами
"""

from django import forms
from .models import Categories, Recipes


class RecipesForm(forms.Form):
    """Устанавливает поля рецептов"""
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    cooking_steps = forms.CharField(widget=forms.Textarea)
    cooking_time = forms.IntegerField()
    image = forms.ImageField()
    author = forms.CharField(max_length=100)
    ingredients = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Categories.objects.all())

class CategoriesForm(forms.Form):
    """Устанавливает поля категорий"""
    name = forms.CharField(max_length=100)


class RecipesCategoriesForm(forms.Form):
    """Устанавливает поля смежной таблици рецептов и категорий"""
    recipes = forms.ModelChoiceField(queryset=Recipes.objects.all())
    category = forms.ModelChoiceField(queryset=Categories.objects.all())