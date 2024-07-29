from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User model
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Foreign key to Category model
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images',
 blank=True, null=True)  # For storing recipe images
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class date_time(models.Model):
        Uploaded_date =models.DateTimeField
        
    def __str__(self):
        return self.name
    
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 

        

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

    

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    following = models.ManyToManyField('self', related_name='follower', symmetrical=False)
