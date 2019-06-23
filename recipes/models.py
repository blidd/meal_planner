from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Ingredient(models.Model):

	SPRING = 'SP'
	SUMMER = 'SU'
	FALL = 'FA'
	WINTER = 'WI'
	ALL_SEASONS = 'AS'

	SEASONALITY_CHOICES = [
		(SPRING, 'Spring'), 
		(SUMMER, 'Summer'),
		(FALL, 'Fall'),
		(WINTER, 'Winter'),
		(ALL_SEASONS, 'All seasons'),
	]

	name = models.CharField(max_length=30, unique=True)
	seasonality = models.CharField(
		max_length=30, 
		choices=SEASONALITY_CHOICES, 
		default=ALL_SEASONS)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)


class Recipe(models.Model):
	name = models.CharField(max_length=50, unique=True)
	likes = models.IntegerField(default=0)
	cuisine = models.CharField(max_length=50, default='world')
	slug = models.SlugField(unique=True)

	# owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipe')
	
	ingredients = models.ManyToManyField(
		Ingredient, 
		through='RecipeItem', 
		related_name='recipes')

	users = models.ManyToManyField(
		User, 
		through='UserRecipe', 
		related_name='recipes')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('add-recipe')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	class Meta:
		ordering = ('name',)


class Instruction(models.Model):
	step_num = models.IntegerField()
	text = models.TextField()
	recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)

	def __str__(self):
		return '%s recipe: step #%d' % (self.recipe_name, self.step_num)


class RecipeItem(models.Model):
	'''
	Custom "through" model between Recipe and Ingredient models.
	'''

	MEASUREMENT_UNITS = [
		('CUP', 'Cups'),
		('TSP', 'Teaspoons'),
		('TBSP', 'Tablespoons'),
		('PCS', 'Pieces'),
		('LBS', 'Pounds'),
		('NA', 'None'),
	]

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	qty = models.IntegerField()
	unit = models.CharField(
		max_length=30,
		choices=MEASUREMENT_UNITS,
		default='NA')

	ingredient_name = models.ForeignKey(
		Ingredient, 
		related_name='recipe_items', 
		on_delete=models.SET_NULL, 
		null=True, 
		blank=True)

	recipe_name = models.ForeignKey(
		Recipe,
		related_name='recipe_items', 
		on_delete=models.CASCADE)

	def __str__(self):
		return "%d %s of %s" % (self.qty, self.unit, self.name)

	class Meta:
		verbose_name = 'Recipe Item'


class UserRecipe(models.Model):
	'''
	Custom "through" model between Recipe and Ingredient models. Allows user
	to specify a meal for which to make the selected recipe.
	'''

	MEAL_TIMES = [
		('BR', 'Breakfast'),
		('LU', 'Lunch'),
		('DI', 'Dinner'),
	]

	meal_time = models.CharField(max_length=30, choices=MEAL_TIMES, default="")
	meal_date = models.DateField(auto_now_add=True)

	user = models.ForeignKey(
		User, 
		related_name='user_recipe', 
		on_delete=models.CASCADE)

	recipe = models.ForeignKey(Recipe,
		related_name='user_recipe',
		on_delete=models.CASCADE)


