from django.db import models
from django.db.models.deletion import PROTECT, CASCADE, SET_NULL 
from django.db.models.fields import FloatField, IntegerField
from datetime import datetime, date 
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
                yield i 
    def names(self):
        store = []
        for i in self.reciperequirment_set.all():
            if not i.stocked():
                store.append(i.ingredient.name)
        return store 

    def sales(self):
        count = 0
        for i in self.purchase_set.all():
            if i.register == Register.objects.last():
                count += 1
        count = str(count)
        return count 
    def get_absolute_url(self):
        return '/ingredient/create'
    def __str__(self):
        return self.title 


class RecipeRequirment(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    required_amount = models.FloatField(default=0)
    def stocked(self):
        return self.ingredient.quantity >= self.required_amount
    def short(self):
        return self.required_amount - self.ingredient.quantity 
    def get_absolute_url(self):
        return "/recipe/create"
    def __str__(self):
        return self.ingredient.name
  
class Register(models.Model):
    daily_bank = models.FloatField(default=500)
    amount_spent = models.FloatField(default=0)
    amount_made = models.FloatField(default=0)
    date = models.DateField(default=date.today) 
    def sales(self):
        lst = []
        for p in self.purchase_set.all():
            if p.menu_item not in lst:
                lst.append([p.menu_item.title, 1])
            else:
                for entry in lst:
                    if entry[0] == p.menu_item.title:
                        entry[1] = entry[1] + 1
        return lst
    def profit(self):
        if self.id > 1:
            return self.daily_bank - Register.objects.get(id=self.id-1).daily_bank
        else:
            return self.daily_bank - 500
    def last(self):
        return self == Register.objects.last()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=SET_NULL, null=True)
    time = models.DateField(default=datetime.now)
    item_name = models.CharField(max_length=100)
    register = models.ForeignKey(Register, on_delete=CASCADE, default=Register.objects.last())
    def save(self, *args, **kwargs):
        self.item_name = self.menu_item.title
        if self.pk is None:
            for i in self.menu_item.reciperequirment_set.all():
                if i.menu_item == self.menu_item:
                    i.ingredient.quantity -= i.required_amount 
                    i.ingredient.save()
        super(Purchase, self).save(*args, **kwargs)


    



