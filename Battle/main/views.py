"""
Файл представлений
"""
from django.shortcuts import render, redirect
from main.models import Recipes, RecipesCategories
from .forms import RecipesForm
from django.core.files.storage import FileSystemStorage

def recipes(request):
    """Отображение рецептов"""
    recipes = Recipes.objects.all()
    return render(request, 'main/recipes.html', {'recipes':recipes})

def recipe(request, recipe_id):
    """Отображение рецепта по id"""
    recipes = Recipes.objects.get(id=recipe_id)
    recipe = {
        "name": recipes.name,
        "image": recipes.image,
        "author": recipes.author,
        "cooking_time": recipes.cooking_time,
        "ingredients": recipes.ingredients,
        "description": recipes.description,
        "cooking_steps": recipes.cooking_steps
    }

    return render(request, 'main/recipe.html', {'recipe':recipe})


def recipe_form(request):
    """Отображение формы добавления, добавление рецепта"""
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipes.objects.create(
                name=data['name'],
                description=data['description'],
                cooking_steps=data['cooking_steps'],
                cooking_time=data['cooking_time'],
                image=f"main/{data['image'].name}/",
                ingredients=data['ingredients'],
                author=data['author'],)
            RecipesCategories.objects.create(
                recipes=recipe,
                category=data['category'],)
            fs = FileSystemStorage(location='main/static/main/', base_url='/main')
            fs.save(data['image'].name, data['image'])
            return redirect('recipe_form')
    else:
        form = RecipesForm()
    return render(request, 'main/recipe_form.html', {'form': form})