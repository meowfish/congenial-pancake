from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    my_context = {
        "my_text":"this is my text",
        "my_number":123,
        "list_of_num":[123,456,789],
    }
    return render(request, "home.html",my_context)
def recipe(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>This is the recipe</h1>")
    return render(request, "recipe.html", {})