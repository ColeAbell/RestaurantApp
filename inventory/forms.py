from django import forms
from .models import Ingredient, Purchase, RecipeRequirment, MenuItem

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem 
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient 
        fields = '__all__' 
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['quantity'].widget.attrs['min'] = 0
class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirment
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['required_amount'].widget.attrs['min'] = 0
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ("menu_item", "time")
