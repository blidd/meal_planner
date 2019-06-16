import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_planner.settings')

import django
django.setup()
from meal_planner.models import Recipe

def populate():

	milk_cookies_recipe = [
		{'name': 'milk',
		 'qty': '5',
		 'unit': 'CUP'},
		{'name': 'cookies',
		 'qty': '6',
		 'unit': 'PCS'}]

	recipes = {'milk_cookies': {'recipe_items': milk_cookies_recipe, 'likes': 0, 'cuisine': 'world'}}
	

if __name__ == '__main__':
	print("Starting Recipes population script...")
	populate()









