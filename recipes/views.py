from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer

@api_view(['POST'])
def add_recipe(request):
    if request.method == 'POST':
        print("hello")
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_recipe_by_id(request, id):
    try:
        recipe = Recipe.objects.get(pk=id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

