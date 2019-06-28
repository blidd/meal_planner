from django.contrib import admin
from recipes.models import Recipe, Ingredient, Instruction, RecipeItem, UserRecipe

# Register your models here.

class RecipeItemInline(admin.TabularInline):
	model = RecipeItem


class InstructionInline(admin.TabularInline):
	model = Instruction


class RecipeAdmin(admin.ModelAdmin):
	inlines = [
		RecipeItemInline,
		InstructionInline,
	]
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(RecipeItem)
admin.site.register(UserRecipe)