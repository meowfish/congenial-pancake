from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_view(request):
    my_context = {
    "my_text": "The domain of you",
    "my_number": 7987,
    "my_list": ["a", "b", "c"]
    }
    return render(request, "home.html", my_context)
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Welcome to my super cool website BRO B)</h1>")
