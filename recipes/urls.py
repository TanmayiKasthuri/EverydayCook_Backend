from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.get_all_recipes),
    path('recipes/<int:id>/', views.get_recipe_by_id),
    path('recipes/add/', views.add_recipe),
]
