from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from fractions import Fraction

from recipes.models import Recipe, RecipeItem, Ingredient, Instruction, UserRecipe
from recipes import forms


class RecipeIndexView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipe_list'  # same as default, but made explicit for greater clarity

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients_list'] = Ingredient.objects.all()
        return context


class RecipeBrowseView(ListView):
    model = Recipe
    template_name = 'recipes/browse_recipes.html'
    context_object_name = 'recipe_list'
    paginate_by = 10


def create_recipe(request):
    if request.method == 'POST':
        form = forms.RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save()
            return redirect('edit_recipe', recipe_name_slug=recipe.slug)

    form = forms.RecipeForm()
    return render(request, 'recipes/create_recipe.html', context={'form': form})


@login_required
def edit_recipe(request, recipe_name_slug):
    recipe = Recipe.objects.get(slug=recipe_name_slug)
    RecipeItemFormset = inlineformset_factory(
        Recipe,
        RecipeItem,
        form=forms.RecipeItemForm,
        fields=('qty', 'unit', 'ingredient', 'description'),
        extra=10)
    InstructionFormset = inlineformset_factory(Recipe, Instruction, fields=('step_num', 'text'), extra=8)

    if request.method == 'POST':
        recipeitem_formset = RecipeItemFormset(request.POST, instance=recipe)
        instruction_formset = InstructionFormset(request.POST, instance=recipe)

        if recipeitem_formset.is_valid() and instruction_formset.is_valid():
            recipeitem_formset.save()
            instruction_formset.save()
            return redirect('show_recipe', recipe_name_slug=recipe.slug)

    recipeitem_formset = RecipeItemFormset(instance=recipe)
    instruction_formset = InstructionFormset(instance=recipe)

    context_dict = {
        'recipeitem_formset': recipeitem_formset,
        'instruction_formset': instruction_formset,
    }

    return render(request, 'recipes/edit_recipe.html', context=context_dict)


def show_recipe(request, recipe_name_slug):
    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        recipe_items = RecipeItem.objects.filter(recipe=recipe)
        instructions = Instruction.objects.filter(recipe_name=recipe)
        context_dict = {
            'recipe': recipe,
            'recipe_items': recipe_items,
            'instructions': instructions,
        }

    except Recipe.DoesNotExist:
        context_dict = {
            'recipe': None,
            'recipe_items': None,
            'instructions': None,
        }

    return render(request, 'recipes/show_recipe.html', context=context_dict)


@login_required
def save_recipe(request, recipe_name_slug):
    recipe = Recipe.objects.get(slug=recipe_name_slug)
    UserRecipeFormset = inlineformset_factory(Recipe, UserRecipe, fields=('meal_time', 'meal_date'), extra=1)
    userrecipe_formset = UserRecipeFormset(instance=recipe)

    if request.method == 'POST':
        userrecipe_formset = UserRecipeFormset(request.POST, instance=recipe)

        if userrecipe_formset.is_valid():
            added_user_recipes = userrecipe_formset.save(commit=False)
            for user_recipe in added_user_recipes:
                user_recipe.user = request.user
                user_recipe.save()

            return redirect('index')

    context_dict = {
        'recipe': recipe,
        'userrecipe_formset': userrecipe_formset,
    }

    return render(request, 'recipes/save_recipe.html', context=context_dict)


class UserProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_recipes = UserRecipe.objects.filter(user=self.request.user).order_by('meal_date', 'meal_time')

        recipe_items = [item 
            for recipe in Recipe.objects.filter(users=self.request.user)
            for item in RecipeItem.objects.filter(recipe=recipe)]

        groceries = {}
        for item in recipe_items:
            key = (item.ingredient.name, item.unit)
            groceries[key] = Fraction(groceries.get(key, 0) + item.qty).limit_denominator()

        context['user_recipes'] = user_recipes
        context['groceries'] = groceries
        context['user'] = self.request.user

        return context


class UserRecipesUpdate(UpdateView):
    """View to handle updating recipe date and time"""

    model = UserRecipe
    fields = ['meal_time', 'meal_date']
    template_name = 'user/user_recipes_update.html'
    success_url = reverse_lazy('my_recipes')


class UserRecipesDelete(DeleteView):
    """View to delete recipe"""

    model = UserRecipe
    template_name = 'user/user_recipes_delete.html'
    context_object_name = 'user_recipe'
    success_url = reverse_lazy('my_recipes')


class UserRecipesDisplay(ListView):
    """Generic class-based view that lists all recipes chosen by a user."""

    model = UserRecipe
    template_name = 'user/user_recipes.html'
    context_object_name = 'user_recipes'

    def get_queryset(self):
        return UserRecipe.objects.filter(user=self.request.user)


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
