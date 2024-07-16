from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    type = models.JSONField()
    category = models.CharField(max_length=100)
    timeCategory = models.CharField(max_length=100)
    tags = models.JSONField()
    image_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=255)
    alternateIngredient = models.JSONField()
    importance = models.CharField(max_length=50)

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='instructions', on_delete=models.CASCADE)
    order = models.IntegerField()
    instruction = models.TextField()
    requiredTime = models.CharField(max_length=50)
    canSkip = models.BooleanField(default=False)
    alternateInstruction = models.CharField(max_length=255, default="none")

