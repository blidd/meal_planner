import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_planner.settings')
django.setup()

from django.contrib.auth.models import User
from recipes.models import Recipe, Ingredient, RecipeItem


def add_ingredients(ingredient_list):
    for ingredient in ingredient_list:
        name = ingredient['name']
        seasonality = ingredient['seasonality']
        Ingredient.objects.create(name=name, seasonality=seasonality)


def add_recipes(recipe_list):
    for recipe in recipe_list:
        name = recipe['name']
        likes = recipe['likes']
        cuisine = recipe['cuisine']

        instance = Recipe.objects.create(name=name, likes=likes, cuisine=cuisine)

        for ingredient_name in recipe['ingredients']:
            ingredient_obj = Ingredient.objects.get(name=ingredient_name)
            instance.ingredients.add(ingredient_obj)

        user_obj = User.objects.get(username=recipe['user'])
        instance.users.add(user_obj)


def populate():

    ingredients = [
        {'name': 'milk', 'seasonality': 'AS'},
        {'name': 'cookies', 'seasonality': 'AS'},
        {'name': 'cheese', 'seasonality': 'AS'},
        {'name': 'dough', 'seasonality': 'AS'},
        {'name': 'tomatoes', 'seasonality': 'AS'},
        {'name': 'butter', 'seasonality': 'AS'},
        {'name': 'eggs', 'seasonality': 'AS'},
        {'name': 'salt', 'seasonality': 'AS'},
    ]

    recipes = [
        {
            'name': 'milk and cookies',
            'likes': 200,
            'cuisine': 'world',
            'ingredients': ['milk', 'cookies'],
            'user': 'brianli'},
        {
            'name': 'pizza',
            'likes': 100,
            'cuisine': 'italian',
            'ingredients': ['cheese', 'dough', 'tomatoes'],
            'user': 'brianli'},
        {
            'name': 'omelette',
            'likes': 300,
            'cuisine': 'french',
            'ingredients': ['eggs', 'butter', 'salt'],
            'user': 'brianli'},
        {
            'name': 'croissant',
            'likes': 500,
            'cuisine': 'french',
            'ingredients': ['butter', 'dough'],
            'user': 'brianli'},
    ]

    add_ingredients(ingredients)
    add_recipes(recipes)


if __name__ == '__main__':
    print("Starting Recipes population script...")
    populate()


# def add_recipe_item(name, qty, units, ingredient_name, recipe_name):
#     ingredient_obj = Ingredient.objects.get(name=ingredient_name)
#     recipe_obj = Recipe.objects.get(name=recipe_name)
#
#     instance = RecipeItem.objects.create(
#         name=name,
#         qty=int(qty),
#         units=units,
#         ingredient=ingredient_obj,
#         recipe=recipe_obj)
#
#
# def add_ri_list_of_lists(ri_list_of_lists):
#     for ri_list in ri_list_of_lists:
#         add_recipe_item(
#             name=ri_list['name'],
#             qty=ri_list['qty'],
#             units=ri_list['units'],
#             ingredient_name=ri_list['ingredient_name'],
#             recipe_name=ri_list['recipe_name'])


# milk_cookies_ingredients = [

#         {'name': 'milk',
#          'qty': '5',
#          'unit': 'CUP',
#          'ingredient_name': 'milk',
#          'recipe_name': 'milk and cookies'},

#         {'name': 'cookies',
#          'qty': '6',
#          'unit': 'PCS',
#          'ingredient_name': 'cookies',
#          'recipe_name': 'milk and cookies'},

#     ]

#     pizza_ingredients = [
#         {'name': 'cheese',
#          'qty': '2',
#          'unit': 'LBS',
#          'ingredient_name': 'cheese',
#          'recipe_name': 'pizza'},
#         {'name': 'dough',
#          'qty': '5',
#          'unit': 'LBS',
#          'ingredient_name': 'dough',
#          'recipe_name': 'pizza'},
#         {'name': 'tomatoes',
#          'qty': '5',
#          'unit': 'CUP',
#          'ingredient_name': 'tomatoes',
#          'recipe_name': 'pizza'},
#     ]

#     croissant_ingredients = [
#         {'name': 'butter',
#          'qty': '5',
#          'unit': 'CUP',
#          'ingredient_name': 'butter',
#          'recipe_name': 'croissant'},
#         {'name': 'dough',
#          'qty': '6',
#          'unit': 'LBS',
#          'ingredient_name': 'dough',
#          'recipe_name': 'croissant'},
#     ]

#     omelette_ingredients = [
#         {'name': 'eggs',
#          'qty': '3',
#          'unit': 'PCS',
#          'ingredient_name': 'eggs',
#          'recipe_name': 'omelette'},
#         {'name': 'butter',
#          'qty': '3',
#          'unit': 'TSP',
#          'ingredient_name': 'butter',
#          'recipe_name': 'omelette'},
#         {'name': 'salt',
#          'qty': '1',
#          'unit': 'TSP',
#          'ingredient_name': 'salt',
#          'recipe_name': 'omelette'},
#     ]