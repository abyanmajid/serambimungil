from django.shortcuts import render, HttpResponse

def home(response):
    context = {}
    return render(response, 'main/home.html', context)

def products(response):
    context = {}
    return render(response, 'main/all_products.html', context)

def regular(response):
    context = {}
    return render(response, 'main/products_by_category.html', context)

def seasonal(response):
    context = {}
    return render(response, 'main/products_by_category.html', context)

def about(response):
    context = {}
    return render(response, 'main/about.html', context)

def contact(response):
    context = {}
    return render(response, 'main/contact.html', context)
