from django import forms
from .models import indiv_recipe

class searchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder" : "name", 
    }))

class recipeCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder" : "name",
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "rows" : 5,
        "cols" : 20,
        "placeholder" : "description", 
    }))
    ingredient = forms.CharField(widget=forms.Textarea(attrs={
        "rows" : 8,
        "cols" : 24,
        "placeholder" : "ingredient",
    }))
    vegan = forms.BooleanField()
    class Meta:
        model = indiv_recipe
        fields = {
            "name",
            "description",
            "ingredient",
            "vegan",
        }

class RawRecipeForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "placeholder" : "name",
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "rows" : 5,
        "cols" : 20,
        "placeholder" : "description", 
    }))
    ingredient = forms.CharField(required=True, widget=forms.Textarea(attrs={
        "rows" : 8,
        "cols" : 24,
        "placeholder" : "ingredient",
    }))
    vegan = forms.BooleanField(required=False)