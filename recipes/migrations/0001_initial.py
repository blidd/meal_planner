# Generated by Django 2.2.1 on 2019-06-23 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('seasonality', models.CharField(choices=[('SP', 'Spring'), ('SU', 'Summer'), ('FA', 'Fall'), ('WI', 'Winter'), ('AS', 'All seasons')], default='AS', max_length=30)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('likes', models.IntegerField(default=0)),
                ('cuisine', models.CharField(default='world', max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_time', models.CharField(choices=[('BR', 'Breakfast'), ('LU', 'Lunch'), ('DI', 'Dinner')], default='', max_length=30)),
                ('meal_date', models.DateField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recipe', to='recipes.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recipe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('unit', models.CharField(choices=[('CUP', 'Cups'), ('TSP', 'Teaspoons'), ('TBSP', 'Tablespoons'), ('PCS', 'Pieces'), ('LBS', 'Pounds'), ('NA', 'None')], default='NA', max_length=30)),
                ('ingredient_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipe_items', to='recipes.Ingredient')),
                ('recipe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_items', to='recipes.Recipe')),
            ],
            options={
                'verbose_name': 'Recipe Item',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.RecipeItem', to='recipes.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='users',
            field=models.ManyToManyField(related_name='recipes', through='recipes.UserRecipe', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_num', models.IntegerField()),
                ('text', models.TextField()),
                ('recipe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
        ),
    ]
