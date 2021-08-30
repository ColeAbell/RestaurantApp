from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.InventoryList.as_view(), name='home'),
    path('menu/create', views.MenuCreate.as_view(), name='createmenu'),
    path('ingredient/create', views.IngredientCreate.as_view(), name='createingredient'),
    path('recipe/create', views.RecipeCreate.as_view(), name='createrecipe'),
    path('recipe/<pk>/update', views.RecipeUpdate.as_view(), name="updaterecipe"),
    path('menu/<pk>/delete', views.MenuDelete.as_view(), name='deletemenu'),
    path("recipe/<pk>/delete", views.RecipeDelete.as_view(), name='deleterecipe'),
    path("menu/<pk>/update", views.MenuUpdate.as_view(), name='updatemenu'),
    path('purchase/create', views.PurchaseCreate.as_view(), name='createpurchase'),
    path("ingredient/<pk>/update", views.IngredientUpdate.as_view(), name='updateingredient'),
    path("ingredient/select_update", views.SelectIngredientUpdate.as_view(), name='update_select_ingredient'),
    path("registration/signup", views.UserCreate.as_view(), name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("/logout", views.logout_view, name='logout'),
]