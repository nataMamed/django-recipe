from django.shortcuts import render
from recipe.models import Recipe


def search_view(request):

    recipe_list = Recipe.objects.order_by('-registration_date').filter(published=True)
    if 'search' in request.GET:
        recipe_to_find = request.GET['search']
        recipe_list = recipe_list.filter(recipe_name__icontains=recipe_to_find)

    data = {    
        'recipes': recipe_list
    }
    return render(request, template_name='recipes/search.html', context=data)
