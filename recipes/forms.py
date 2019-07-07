from django import forms
# from django.forms import inlineformset_factory
from recipes.models import Recipe, RecipeItem, UserRecipe


class RecipeForm(forms.ModelForm):

	class Meta:
		model = Recipe
		fields = ['name', 'cuisine']


class RecipeItemForm(forms.ModelForm):

	class Meta:
		model = RecipeItem
		fields = '__all__'


class UserRecipeForm(forms.ModelForm):

	class Meta:
		model = UserRecipe
		fields = '__all__'


# RecipeItemInlineFormSet = inlineformset_factory(Recipe, RecipeItem, form=RecipeItemForm, extra=3)
