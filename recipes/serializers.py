# from rest_framework import serializers
# from .models import Recipe, Ingredient, Instruction

# class IngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredient
#         fields = '__all__'

# class InstructionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Instruction
#         fields = '__all__'

# class RecipeSerializer(serializers.ModelSerializer):
#     ingredients = IngredientSerializer(many=True)
#     print(ingredients)
#     instructions = InstructionSerializer(many=True)

#     class Meta:
#         model = Recipe
#         fields = '__all__'

#     def create(self, validated_data):
#         ingredients_data = validated_data.pop('ingredients')
#         instructions_data = validated_data.pop('instructions')
#         recipe = Recipe.objects.create(**validated_data)
#         for ingredient_data in ingredients_data:
#             Ingredient.objects.create(recipe=recipe, **ingredient_data)
#         for instruction_data in instructions_data:
#             Instruction.objects.create(recipe=recipe, **instruction_data)
#         return recipe


from rest_framework import serializers
from .models import Recipe, Ingredient, Instruction

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient', 'alternateIngredient', 'importance']

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ['order', 'instruction', 'requiredTime', 'canSkip', 'alternateInstruction']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    instructions = InstructionSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        instructions_data = validated_data.pop('instructions')
        recipe = Recipe.objects.create(**validated_data)
        
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        
        for instruction_data in instructions_data:
            Instruction.objects.create(recipe=recipe, **instruction_data)
        
        return recipe
