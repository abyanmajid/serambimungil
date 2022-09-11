from django.shortcuts import render, HttpResponse

def home(response):
    context = {}
    return render(response, 'main/home.html', context)

def menu(response):
    context = {}
    return render(response, 'main/menu.html', context)

def about(response):
    context = {}
    return render(response, 'main/about.html', context)

def contact(response):
    context = {}
    return render(response, 'main/contact.html', context)
