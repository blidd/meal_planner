from django.contrib import admin
from recipes.models import Recipe, Ingredient, Instruction, RecipeItem

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
	pass


class IngredientAdmin(admin.ModelAdmin):
	pass


class InstructionAdmin(admin.ModelAdmin):
	pass


class RecipeItemAdmin(admin.ModelAdmin):
	pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Instruction, InstructionAdmin)
admin.site.register(RecipeItem, RecipeItemAdmin)
