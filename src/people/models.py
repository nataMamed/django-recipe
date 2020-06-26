from django.db import models

class People(models.Model):

    person_name  = models.CharField(max_length=200)
    person_email = models.CharField(max_length=200)


    def __str__(self):
        return self.person_name