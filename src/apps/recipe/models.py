from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Recipe(models.Model):

    person             = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name        = models.CharField(max_length=200)
    category           = models.CharField(max_length=100)
    ingredients        = models.TextField()
    preparation_method = models.TextField()
    preparation_time   = models.IntegerField()
    revenue            = models.CharField(max_length=50)
    published          = models.BooleanField(default=False)
    registration_date  = models.DateTimeField(default=datetime.now, blank=True)
    recipe_photo       = models.ImageField(upload_to='photo/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.recipe_name

    