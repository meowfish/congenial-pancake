from django.db import models

# Create your models here.
class main_menu(models.Model):
    search = models.CharField(max_length=100)
    def __str__(self):
        return self.search

class indiv_recipe(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True, default="this is food")
    description = models.TextField(blank=True)
    ingredient = models.TextField(blank=False)
    vegan = models.BooleanField(blank=True)
    #menu = models.ForeignKey(main_menu, related_name="main_menu")
    def __str__(self):
        return self.name

