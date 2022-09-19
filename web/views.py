from django.shortcuts import render, HttpResponse

# create your views here.

def Home(request):
    return render(request, 'web/home.html',)


def About(request):
    return render(request, 'web/about.html',)


def Contact(request):
    return render(request, 'web/contact.html',)