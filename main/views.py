from math import prod
from django.http import Http404
from queue import PriorityQueue
from django.shortcuts import render
from main.models import Product

def home(response):
    context = {}
    return render(response, 'main/home.html', context)

def menu(response):
    products = Product.objects.all()
    context = {'products': products}
    return render(response, 'main/menu.html', context)

def about(response):
    context = {}
    return render(response, 'main/about.html', context)

def contact(response):
    context = {}
    return render(response, 'main/contact.html', context)
# def login(response):
#     context = {}
#     return render(response, 'main/login.html', context)