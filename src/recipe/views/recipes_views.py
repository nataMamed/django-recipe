from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from recipe.models import Recipe
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_view(request):
    
    recipes          = Recipe.objects.order_by('-registration_date').filter(published=True)
    paginator        = Paginator(recipes, per_page=6)
    page             = request.GET.get('page')
    recipes_per_page = paginator.get_page(page)

    data ={
        "recipes": recipes_per_page
    }

    return render(request, template_name='recipes/index.html', context=data)

def recipe_view(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe_to_show = {
        "recipe": recipe
    }

    return render(request, template_name='recipes/recipe.html', context=recipe_to_show)

def create_recipe_view(request):

    if request.method == 'POST':
        recipe_name        = request.POST['nome_receita']
        ingredients        = request.POST['ingredientes']
        preparation_method = request.POST['modo_preparo']
        preparation_time   = request.POST['tempo_preparo']
        revenue            = request.POST['rendimento']
        category           = request.POST['categoria']
        recipe_photo       = request.FILES['foto_receita']

        user = get_object_or_404(User, pk=request.user.id)

        recipe = Recipe.objects.create(
            person=user,
            recipe_name=recipe_name,
            ingredients=ingredients,
            preparation_method=preparation_method,
            preparation_time=preparation_time,
            revenue=revenue,
            category=category,
            recipe_photo=recipe_photo
        )
        return redirect(to='dashboard')
    else:
        return render(request, template_name='recipes/create_recipe.html')

def delete_recipe(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()

    return redirect(to='dashboard')

def update_recipe(request, recipe_id):


    recipe  = get_object_or_404(Recipe, pk=recipe_id)
    context = {
        'recipe':recipe
    }
    
    return render(request, template_name='recipes/update_recipe.html', context=context)

def refresh_recipe(request):

    if request.method == 'POST':

        recipe_id = request.POST['receita_id']

        recipe                    = Recipe.objects.get(pk=recipe_id)
        recipe.recipe_name        = request.POST['nome_receita']
        recipe.ingredients        = request.POST['ingredientes']
        recipe.preparation_method = request.POST['modo_preparo']
        recipe.preparation_time   = request.POST['tempo_preparo']
        recipe.revenue            = request.POST['rendimento']
        recipe.category           = request.POST['categoria']

        if 'foto_receita' in request.FILES:
            recipe.recipe_photo = request.FILES['foto_receita']

        recipe.save()
        return redirect(to='dashboard')