# Generated by Django 2.2.1 on 2019-06-25 02:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeitem',
            old_name='ingredient_name',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='recipeitem',
            old_name='recipe_name',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='recipes', through='recipes.UserRecipe', to=settings.AUTH_USER_MODEL),
        ),
    ]
