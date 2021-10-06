from django.conf.urls import url
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
    path("ingredient/<pk>/update", views.IngredientUpdate.as_view(), name='updateingredient'),
    path("ingredient/select_update", views.SelectIngredientUpdate.as_view(), name='update_select_ingredient'),
    path("registration/signup", views.UserCreate.as_view(), name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout", views.logout_view, name='logout'),
    path("ingredient/select_delete", views.SelectIngredientDelete.as_view(), name='delete_select_ingredient'),
    path("ingredient/<pk>/delete", views.IngredientDelete.as_view(), name='deleteingredient'),
    path("register", views.newbank, name='createregister'),
    path("r'^restock/(?P<title>\w+)/(?P<amount>\w+)/", views.restock, name="restock"),
    path("r'^restock/(?P<item>\w+)/", views.createpurchase, name='purchase'),
    path("financials", views.RegisterView.as_view(), name='viewregister'),
]