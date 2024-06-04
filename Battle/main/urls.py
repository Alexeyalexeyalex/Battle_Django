"""
Установка путей и привязка представлений
"""
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.recipes, name='recipes'),
    path('all/', views.recipes, name='recipes'),
    path('recipes/recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipe/form/', views.recipe_form, name='recipe_form'),
]
