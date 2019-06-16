from django.urls import path
from recipes import views

urlpatterns = [
	path('', views.RecipeIndex.as_view(), name='index'),
	path('create_recipe/', views.create_recipe, name='create_recipe'),
	path('<slug:recipe_name_slug>/edit_recipe/', views.edit_recipe, name='edit_recipe'),
	path('<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),	
]