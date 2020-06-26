from django.contrib import admin
from .models import People

class ListingPeople(admin.ModelAdmin):

    list_display       = ('id','person_name','person_email')
    list_display_links = ('id','person_name')
    search_fields      = ('person_name',)
    list_per_pege      = 3

admin.site.register(People, ListingPeople)