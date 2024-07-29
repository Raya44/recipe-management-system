from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, Rating
from .forms import RatingForm

def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.recipe = recipe
            rating.save()
            return redirect('recipe_detail', pk=recipe_id)
    else:
        form = RatingForm(initial={'recipe': recipe})
    return render(request, 'rate_recipe.html', {'recipe': recipe, 'form': form})


 
# Create your views here.



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request , 'logout.html')

def login_view(request):
    form = AuthenticationForm(request , data = request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request , user)
        return redirect('home')
    context = {
        'form' : form
    }
    return render(request , 'login.html' , context) 

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
    context = {
        'form': form
    }
    return render(request , 'signup.html' , context)
    
    
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list') 
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


@login_required
def home(request):
    posts = Recipe.objects.all()
    return render(request , 'home.html' , {'posts':posts})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def create_post(request):
    form = RecipeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form' : form
    }
    return render(request , 'create_post.html' , context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 
 'register.html', {'form': form})


def recipe_update(request , pk):
    post = Recipe.objects.get(pk = pk)
    form = RecipeForm(instance=post)
    if request.method == 'POST':
        form = RecipeForm(request.POST , instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'post' : post,
        'form' : form
    }
    return render(request , 'post_update.html' , context)


def recipe_delete(request , pk):
    post = Recipe.objects.get(pk = pk )
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post' : post
    }
    return render(request , 'post_delete.html' , context)

