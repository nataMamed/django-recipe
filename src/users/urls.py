from django.urls import path
from . import views

urlpatterns = [
    path('singup', views.singup_view, name='singup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('create/recipe', views.create_recipe_view, name='create_recipe'),
    path('delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('update/<int:recipe_id>', views.update_recipe, name='update_recipe'),  
    path('refresh_recipe', views.refresh_recipe, name='refresh_recipe')

]
