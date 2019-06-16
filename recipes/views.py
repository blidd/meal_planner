from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView
from django.forms import inlineformset_factory
from recipes.models import Recipe, RecipeItem, Ingredient, Instruction

from .forms import RecipeForm


class RecipeIndex(ListView):
	model = Recipe
	template_name = 'recipes/index.html'
	context_object_name = 'recipe_list' # same as default, but made explicit for greater clarity

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['ingredients_list'] = Ingredient.objects.all()
		return context


def create_recipe(request):

	if request.method == 'POST':
		form = RecipeForm(request.POST)

		if form.is_valid():
			recipe = form.save()
			return redirect('edit_recipe', recipe_name_slug=recipe.slug)

	form = RecipeForm()
	return render(request, 'recipes/create_recipe.html', context={'form': form})


def edit_recipe(request, recipe_name_slug):
	recipe = Recipe.objects.get(slug=recipe_name_slug)
	RecipeItemFormset = inlineformset_factory(Recipe, RecipeItem, fields=('name','qty','unit','ingredient_name'), extra=10)
	InstructionFormset = inlineformset_factory(Recipe, Instruction, fields=('step_num', 'text'), extra=5)

	if request.method == 'POST':
		recipeitem_formset = RecipeItemFormset(request.POST, instance=recipe)
		instruction_formset = InstructionFormset(request.POST, instance=recipe)

		if recipeitem_formset.is_valid() and instruction_formset.is_valid():
			recipeitem_formset.save()
			instruction_formset.save()
			return redirect('show_recipe', recipe_name_slug=recipe.slug)

	recipeitem_formset = RecipeItemFormset(instance=recipe)
	instruction_formset = InstructionFormset(instance=recipe)

	context_dict = {'recipeitem_formset': recipeitem_formset, 'instruction_formset': instruction_formset}
	return render(request, 'recipes/edit_recipe.html', context=context_dict)


def show_recipe(request, recipe_name_slug):
	context_dict = {}

	try:
		recipe = Recipe.objects.get(slug=recipe_name_slug)
		recipe_items = RecipeItem.objects.filter(recipe_name=recipe)
		instructions = Instruction.objects.filter(recipe_name=recipe)
		context_dict['recipe'] = recipe
		context_dict['recipe_items'] = recipe_items
		context_dict['instructions'] = instructions

	except Recipe.DoesNotExist:
		context_dict['recipe'] = None
		context_dict['recipe_items'] = None
		context_dict['instructions'] = None

	return render(request, 'recipes/show_recipe.html', context=context_dict)


# class RecipeCreate(CreateView):
# 	model = Recipe
# 	template_name = 'recipes/add_recipe.html'
# 	form_class = RecipeForm

# 	def get_context_data(self, **kwargs):
# 		data = super(RecipeCreate, self).get_context_data(**kwargs)
# 		if self.request.POST:
# 			data['recipe_items'] = RecipeItemInlineFormSet(self.request.POST)
# 		else:
# 			data['recipe_items'] = RecipeItemInlineFormSet()
# 		return data

# 	def form_valid(self, form):
# 		context = self.get_context_data()
# 		recipe_items = context['recipe_items']

# 		with transaction.atomic():
# 			self.object = form.save()

# 			if recipe_items.is_valid():
# 				recipe_items.instance = self.object
# 				recipe_items.save()

# 		return super(RecipeCreate, self).form_valid(form)