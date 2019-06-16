from django import forms
# from django.forms import inlineformset_factory
from recipes.models import Recipe, RecipeItem


class RecipeForm(forms.ModelForm):

	class Meta:
		model = Recipe
		fields = ['name', 'cuisine']


class RecipeItemForm(forms.ModelForm):

	class Meta:
		model = RecipeItem
		exclude = ()


# RecipeItemInlineFormSet = inlineformset_factory(Recipe, RecipeItem, form=RecipeItemForm, extra=3)
