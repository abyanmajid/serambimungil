from django.shortcuts import render, HttpResponse

def home(response):
    return HttpResponse('successful!!!')