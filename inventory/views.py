from django.shortcuts import render, redirect 
from .models import Ingredient, RecipeRequirment, MenuItem, Purchase
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView
from .forms import MenuForm, IngredientForm, RecipeForm, PurchaseForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth import logout

# Create your views here.
class InventoryList(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"
    def get_context_data(self):
        context = super().get_context_data()
        context['Recipe'] = RecipeRequirment.objects.all()
        context['Menu'] = MenuItem.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        context['Purchase'] = Purchase.objects.all()
        return context
class MenuCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'inventory/createmenu.html'
    form_class = MenuForm 
class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient 
    template_name = 'inventory/createingredient.html'
    form_class = IngredientForm
    def get_context_data(self):
        context = super().get_context_data()
        context['ingredients'] = Ingredient.objects.all()
        return context
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirment
    template_name = 'inventory/createrecipe.html'
    form_class = RecipeForm
class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirment
    template_name = 'inventory/updaterecipe.html'
    form_class = RecipeForm 
    success_url = reverse_lazy("home")
class MenuDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem 
    template_name = "inventory/deletemenu.html"
    form_class = MenuForm 
    success_url = reverse_lazy("home")
class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirment
    template_name = "inventory/deleterecipe.html"
    form_class = RecipeForm
    success_url = reverse_lazy("home")
class MenuUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/updatemenu.html"
    form_class = MenuForm
    success_url = reverse_lazy("home")
class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase 
    template_name = "inventory/createpurchase.html"
    form_class = PurchaseForm
    success_url = reverse_lazy("home")
class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient 
    template_name = "inventory/updateingredient.html"
    form_class = IngredientForm
    success_url = reverse_lazy("home")
class SelectIngredientUpdate(LoginRequiredMixin, TemplateView):
    template_name = "inventory/selectingredient_update.html"
    def get_context_data(self):
        context = super().get_context_data()
        context['ingredients'] = Ingredient.objects.all()
        return context
class UserCreate(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login") 
def logout_view(request):
    logout(request)
    return redirect("home")

    


     



