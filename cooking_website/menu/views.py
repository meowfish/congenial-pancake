from django.shortcuts import render
from django.http import HttpResponse
from .forms import recipeCreateForm, RawRecipeForm, searchForm
from .models import indiv_recipe
def search_view(request):
    search = searchForm()
    context={
        "search" : search,
    }
    return render(request, "recipe/search.html",context)
def recipe_create_view(request):
    raw_form = RawRecipeForm()
    if request.method == "POST":
        raw_form = RawRecipeForm(request.POST)
        if raw_form.is_valid():
            print(raw_form.cleaned_data)
            indiv_recipe.objects.create(**raw_form.cleaned_data)
            raw_form = RawRecipeForm(None)
        else:
            raw_form = RawRecipeForm(None)
            print(raw_form.errors)
    context={
        "form" : raw_form
    }
    return render(request, "recipe/create.html",context)

""" def recipe_create_view(request):
    if request.method == "POST":
        print(request.POST.get("name"))
        print(request.POST.get("description"))
   
    context={}
    return render(request, "recipe/create.html",context)
 """


""" def recipe_create_view(request):
    form = recipeCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = recipe_create_view(request)
    context={
        "form" : form
    }
    return render(request, "recipe/create.html",context)
 """
def recipe_detail_view(request):
    obj = indiv_recipe.objects.get(id=4)
    context={
        "object" : obj
    }
    return render(request, "recipe/detail.html",context)
# Create your views here.
