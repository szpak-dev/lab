from django.contrib import admin

from .models import Dish
from .models import RecipeIngredient
from .models import Ingredient
from .models import Recipe
from .models import RecipeStep


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    exclude = ['created_at']


class RecipeIngredientInline(admin.StackedInline):
    exclude = ['created_at']
    model = RecipeIngredient
    extra = 1


class RecipeStepInline(admin.StackedInline):
    exclude = ['created_at']
    model = RecipeStep
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes')
    exclude = ['created_at']
    inlines = [
        RecipeIngredientInline,
        RecipeStepInline,
    ]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'public_id', 'daily_limit')
    exclude = ['created_at']
