from django.urls import path
from . import views 

urlpatterns = [
   path('', views.index_view, name='index'),
   path('<int:recipe_id>', views.recipe_view, name='recipe'),
   path('search', views.search_view, name='search'),
]
