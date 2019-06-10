from django.shortcuts import render
from recipes.models import Recipe, Ingredient

# Create your views here.

def index(request):

	recipe_list = Recipe.objects.order_by('-name')
	ingredients_list = Ingredient.objects.order_by('-name')

	context_dict = {
		'recipe_list': recipe_list,
		'ingredients_list': ingredients_list,
	}

	return render(request, 'recipes/index.html', context=context_dict)