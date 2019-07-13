from django.urls import path
from recipes import views

urlpatterns = [
	path('', views.RecipeIndexView.as_view(), name='index'),
	path('browse/page<int:page>/', views.RecipeBrowseView.as_view(), name='browse'),
	path('create_recipe/', views.create_recipe, name='create_recipe'),
	path('<slug:recipe_name_slug>/edit_recipe/', views.edit_recipe, name='edit_recipe'),
	path('<slug:recipe_name_slug>/save_recipe/', views.save_recipe, name='save_recipe'),
	path('<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),
]