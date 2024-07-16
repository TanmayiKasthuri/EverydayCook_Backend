from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.get_all_recipes),
    path('recipes/<int:id>/', views.get_recipe_by_id),
    path('recipes/add/', views.add_recipe),
    path('recipes/<int:recipe_id>/ingredients/', views.get_ingredients_by_recipe, name='get_ingredients_by_recipe'),
    path('recipes/<int:recipe_id>/instructions/', views.get_instructions_by_recipe, name='get_instructions_by_recipe'),
]
