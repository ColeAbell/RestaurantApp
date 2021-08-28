from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import FloatField, IntegerField
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=20, validators=[MinValueValidator(0)])
    price = models.FloatField(default=0, validators=[MinValueValidator(0)])
    unit_size = models.CharField(max_length=100)
    def get_absolute_url(self):
        return '/ingredient/create'
    def __str__(self):
        return self.name 
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0, validators=[MinValueValidator(5.00)])
    description = models.CharField(max_length=200)
    def available(self):
        return all(i.stocked() for i in self.reciperequirment_set.all())
    def ingreds(self):
        for i in self.reciperequirment_set.all():
            yield i
    def need(self):
        for i in self.reciperequirment_set.all():
            if not i.stocked():
                yield [i.ingredient.name, (i.required_amount - i.ingredient.quantity)]
    def sales(self):
        count = 0
        for i in self.purchase_set.all():
            count += 1
        count = str(count)
        return count
    def get_absolute_url(self):
        return '/ingredient/create'
    def __str__(self):
        return self.title


class RecipeRequirment(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    required_amount = models.FloatField(default=0)
    def stocked(self):
        return self.ingredient.quantity >= self.required_amount
    def get_absolute_url(self):
        return "/recipe/create"
    def __str__(self):
        return self.ingredient.name
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=PROTECT)
    time = models.DateField(default=datetime.now)
    def save(self, *args, **kwargs):
        if self.pk is None:
            for i in self.menu_item.reciperequirment_set.all():
                if i.menu_item == self.menu_item:
                    i.ingredient.quantity -= i.required_amount 
                    i.ingredient.save()
        super(Purchase, self).save(*args, **kwargs)   


    



