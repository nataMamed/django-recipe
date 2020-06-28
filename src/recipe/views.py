from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe


def index_view(request):

    
    recipes = Recipe.objects.order_by('-registration_date').filter(published=True)
    data ={
        "recipes": recipes
    }

    return render(request, template_name='index.html', context=data)

def recipe_view(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_to_show = {
        "recipe": recipe
    }

    return render(request, template_name='recipe.html', context=recipe_to_show)

def search_view(request):

    recipe_list = Recipe.objects.order_by('-registration_date').filter(published=True)
    if 'search' in request.GET:
        recipe_to_find = request.GET['search']
        if search_view:
            recipe_list = recipe_list.filter(recipe_name__icontains=recipe_to_find)

    data = {    
        'recipes': recipe_list
    }
    return render(request, template_name='search.html', context=data)