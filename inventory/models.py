from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import FloatField, IntegerField

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
class MenuItem(models.Model):
    title = models.CharField(max_length=200, default='Pizza')
    price = models.FloatField(default=0)
    availability = models.BooleanField(default=True)
    is_seasonal = models.BooleanField(default=False)
    description = models.CharField(max_length=200)
    def ingred(self, ingredients):
        use = ''
        for i in ingredients:
            if i.menu_item == self:
                use += i.ingredient + ','
        return use

class RecipeRequirment(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField(default=0)
    def check_quantity(self):
        return self.ingredient.amount >= self.quantity
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=PROTECT)
    time = models.DateField()


