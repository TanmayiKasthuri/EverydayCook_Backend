from django.contrib import admin
#from .models import AlternateIngredient
from .models import Recipe
from .models import Ingredient
from .models import Instruction
# Register your models here.
#admin.site.register(AlternateIngredient)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
