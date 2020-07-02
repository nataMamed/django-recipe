from django.urls import path
from .views import *

urlpatterns = [
   path('', index_view, name='index'),
   path('<int:recipe_id>', recipe_view, name='recipe'),
   path('search', search_view, name='search'),
   path('create/recipe', create_recipe_view, name='create_recipe'),
   path('delete/<int:recipe_id>', delete_recipe, name='delete_recipe'),
   path('update/<int:recipe_id>', update_recipe, name='update_recipe'),  
   path('refresh_recipe', refresh_recipe, name='refresh_recipe')
]
