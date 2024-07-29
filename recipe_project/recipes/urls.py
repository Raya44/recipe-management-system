from django.contrib import admin 
from django.urls import path , include
from . import views


# Your URL patterns here (e.g., path('recipes/', include('recipes.recipe_urls')))
 # Your URL patterns here
urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('', views.recipe_list, name='recipe_list'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('register/', views.register, name='register'),
    
     
]

