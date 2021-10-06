from django.db.models.signals import pre_save, post_save 
from django.dispatch import receiver 
from .models import Ingredient, Purchase, MenuItem, RecipeRequirment, Register

@receiver(post_save, sender=Ingredient)
def purchase_new_ingredient(sender, instance, created, **kwargs):
    if created:
        n = Register.objects.last()
        n.daily_bank -= (instance.quantity * instance.price)
        n.amount_spent += (instance.quantity * instance.price)
        n.save()
    else:
        pass 

@receiver(pre_save, sender=Ingredient)
def purchase_more_ingredient(sender, instance, **kwards):
    if instance.id is None:
        pass
    else: 
        current = instance 
        previous = Ingredient.objects.get(id=instance.id)
        if current.quantity > previous.quantity:
            diff = (current.quantity - previous.quantity)
            n = Register.objects.last()
            n.daily_bank -= (current.price * diff)
            n.amount_spent += (current.price * diff)
            n.save()
        else:
            pass

@receiver(post_save, sender=Purchase)
def sale(sender, instance, created, **kwargs):
    if created:
        n = Register.objects.last()
        n.daily_bank += instance.menu_item.price
        n.amount_made += instance.menu_item.price 
        n.save()
    else:
        pass
@receiver(pre_save, sender=Register)
def closing_restock(sender, instance, **kwargs):
    if instance.id is None:
        for k in RecipeRequirment.objects.all():
            if not k.stocked():
                k.ingredient.quantity += k.short()
                k.ingredient.save()
    else:
        pass
@receiver(post_save, sender=Register)
def set_register(sender, instance, created, **kwargs):
    if created:
        if instance.id > 1:
            old = instance.id - 1
            instance.daily_bank = Register.objects.get(id=old).daily_bank
            instance.save()
    else:
        pass






        
