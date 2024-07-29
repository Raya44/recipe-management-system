from django import forms
from .models import Recipe , Rating
import crispy_forms.helper as fh

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields ='__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = fh.FormHelper()
        self.helper.form_id = 'id-recipe-form'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = fh.Layout(
            'title',
            'description',
            'ingredients',
            'instructions',
            'image',
            'category',
            fh.Submit('submit', 'Create Recipe')
        )
        
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        

        
        


