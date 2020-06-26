from django.shortcuts import render
from .models import Recipe


def index_view(request):

    
    recipes = Recipe.objects.order_by('-registration_date').filter(published=True)
    data ={
        "recipes": recipes
    }

    return render(request, template_name='index.html', context=data)

def recipe_view(request):

    return render(request, template_name='recipe.html')
