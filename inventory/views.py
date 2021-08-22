from django.shortcuts import render 
from .models import Ingredient, RecipeRequirment, MenuItem, Purchase
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView


# Create your views here.
class InventoryList(TemplateView):
    template_name = "inventory/home.html"
    def get_context_data(self):
        context = super().get_context_data()
        context['Recipe'] = RecipeRequirment.objects.all()
        context['Menu'] = MenuItem.objects.all()
        return context
    def use_this(self, instance):
        use = ''
        for m in Recipe:
            if m.menu_item == instance:
                use += m.ingredient + ','
        return use
