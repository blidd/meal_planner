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

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name


class Recipe(models.Model):
	name = models.CharField(max_length=50, unique=True)
	likes = models.IntegerField(default=0)
	cuisine = models.CharField(max_length=50, default='world')
	slug = models.SlugField(unique=True)

	# owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recipe')
	users = models.ManyToManyField(User, related_name='recipes')

	
	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('add-recipe')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)


class RecipeItem(models.Model):

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

	# each recipe item maps to only ONE ingredient
	ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	# each recipe item maps to only ONE recipe
	recipe_name = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return "%d %s of %s" % (self.qty, self.unit, self.recipe_name)

	class Meta:
		verbose_name = 'Recipe Item'


class Instruction(models.Model):
	step_num = models.IntegerField()
	text = models.TextField()
	recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE)

	def __str__(self):
		return '%s recipe: step #%d' % (self.recipe_name, self.step_num)




