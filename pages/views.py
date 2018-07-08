from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>HELLO WORLD</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about Nutantech",
        "my_number": 1234
    }
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


