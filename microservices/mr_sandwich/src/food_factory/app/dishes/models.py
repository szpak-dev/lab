from django.db import models
from datetime import datetime


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories_per_100g = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
    )
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_grams = models.FloatField()
    quantity_label = models.CharField(max_length=16)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.ingredient.name


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    instructions = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{} > {}'.format(self.recipe.name, self.ingredient.name)


class Dish(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    description = models.TextField()
    daily_limit = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class DishDailyAvailability(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    day = models.DateField(default=datetime.now)
    available_count = models.IntegerField()
    revision = models.IntegerField(default=1)


class DishReservation(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=64)
    ttl_minutes = models.IntegerField(default=15)
    created_at = models.DateTimeField(default=datetime.now)
