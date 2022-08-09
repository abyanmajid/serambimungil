from django.shortcuts import render, HttpResponse

def home(response):
    return HttpResponse('home')

def products(response):
    return HttpResponse('products')

def regular(response):
    return HttpResponse('regular')

def seasonal(response):
    return HttpResponse('seasonal')

def about(response):
    return HttpResponse('about')

def contact(response):
    return HttpResponse('contact')
