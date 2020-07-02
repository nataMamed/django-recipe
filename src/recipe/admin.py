from django.contrib import admin
from .models import Recipe


class ListingRecipes(admin.ModelAdmin):

    list_display       = ('id','recipe_name','category','preparation_time','published')
    list_display_links = ('id','recipe_name')
    search_fields      = ('recipe_name',)
    list_editable      = ('published',)
    list_filter        = ('category',)
    list_per_page      = 5

admin.site.register(Recipe, ListingRecipes)