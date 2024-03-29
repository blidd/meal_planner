"""meal_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django.contrib
# from django.contrib import admin
from django.urls import path
from django.urls import include

from recipes import views

urlpatterns = [
    path('', views.RecipeIndexView.as_view(), name='index'),

    path('users/my_profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('users/my_profile/my_recipes', views.UserRecipesDisplay.as_view(), name='my_recipes'),
    path('users/my_profile/my_recipes/update/<int:pk>', views.UserRecipesUpdate.as_view(), name='update_recipe'),
    path('users/my_profile/my_recipes/delete/<int:pk>', views.UserRecipesDelete.as_view(), name='delete_recipe'),

    path('admin/', django.contrib.admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]