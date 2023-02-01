from math import prod
from django.http import Http404
from queue import PriorityQueue
from django.shortcuts import render
from main.models import Product, Home
from .forms import MottoForm, QualityForm_1, QualityForm_2, QualityForm_3, FeaturedProductForm_1, FeaturedProductForm_2, FeaturedProductForm_3
from django.http import HttpResponseRedirect

def home(response):
    home = Home.objects.get(id=1)
    
    context = {
        # Motto
        'motto': home.motto,
        
        # Qualities
        'quality_1_heading': home.quality_1_heading,
        'quality_1_caption': home.quality_1_caption,
        'quality_2_heading': home.quality_2_heading,
        'quality_2_caption': home.quality_2_caption,
        'quality_3_heading': home.quality_3_heading,
        'quality_3_caption': home.quality_3_caption,
        
        # Best Sellers
        'bestseller_1_name': home.bestseller_1_name,
        'bestseller_1_caption': home.bestseller_1_caption,
        'bestseller_1_description': home.bestseller_1_description,
        'bestseller_1_image': home.bestseller_1_image,
        'bestseller_2_name': home.bestseller_2_name,
        'bestseller_2_caption': home.bestseller_2_caption,
        'bestseller_2_description': home.bestseller_2_description,
        'bestseller_2_image': home.bestseller_2_image,
        'bestseller_3_name': home.bestseller_3_name,
        'bestseller_3_caption': home.bestseller_3_caption,
        'bestseller_3_description': home.bestseller_3_description,
        'bestseller_3_image': home.bestseller_3_image,
    }
    
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

def login(response):
    context = {}
    return render(response, 'main/login.html', context)

def edit_home(response):
    
    if response.method == 'POST':
        # Get Home Object
        home = Home.objects.get(id=1)
        
        # Retain Data
        mottoform = MottoForm(response.POST)
        qualityform_1 = QualityForm_1(response.POST)
        qualityform_2 = QualityForm_2(response.POST)
        qualityform_3 = QualityForm_3(response.POST)
        featuredproductform_1 = FeaturedProductForm_1(response.POST)
        featuredproductform_2 = FeaturedProductForm_2(response.POST)
        featuredproductform_3 = FeaturedProductForm_3(response.POST)
        
        # MOTTO FORM
        if mottoform.is_valid():
            # Update Motto
            new_motto = mottoform.cleaned_data['motto']
            home.motto = new_motto
            home.save()
            return HttpResponseRedirect('/')
        
        # QUALITY FORMS
        elif qualityform_1.is_valid():
            # Update Quality 1
            new_heading = qualityform_1.cleaned_data['heading']
            new_caption = qualityform_1.cleaned_data['caption']
            home.quality_1_heading = new_heading
            home.quality_1_caption = new_caption
            home.save()
            return HttpResponseRedirect('/')
        
        elif qualityform_2.is_valid():
            # Update Quality 2
            new_heading = qualityform_2.cleaned_data['heading']
            new_caption = qualityform_2.cleaned_data['caption']
            home.quality_2_heading = new_heading
            home.quality_2_caption = new_caption
            home.save()
            return HttpResponseRedirect('/')
        
        elif qualityform_3.is_valid():
            # Update Quality 3
            new_heading = qualityform_3.cleaned_data['heading']
            new_caption = qualityform_3.cleaned_data['caption']
            home.quality_3_heading = new_heading
            home.quality_3_caption = new_caption
            home.save()
            return HttpResponseRedirect('/')
        
        # FEATURED PRODUCTS FORM
        elif featuredproductform_1.is_valid():
            # Update Best Seller 1
            new_name = featuredproductform_1.cleaned_data['name']
            new_caption = featuredproductform_1.cleaned_data['caption']
            new_description = featuredproductform_1.cleaned_data['description']
            new_image = featuredproductform_1.cleaned_data['image']
            home.bestseller_1_name = new_name
            home.bestseller_1_caption = new_caption
            home.bestseller_1_description = new_description
            home.bestseller_1_image = new_image
            home.save()
            return HttpResponseRedirect('/')
    
    else:
        mottoform = MottoForm()
        qualityform_1 = QualityForm_1()
        qualityform_2 = QualityForm_2()
        qualityform_3 = QualityForm_3()
        featuredproductform_1 = FeaturedProductForm_1()
        featuredproductform_2 = FeaturedProductForm_2()
        featuredproductform_3 = FeaturedProductForm_3()

    context = {
        'mottoform': mottoform,
        'qualityform_1': qualityform_1,
        'qualityform_2': qualityform_2,
        'qualityform_3': qualityform_3,
        'featuredproductform_1': featuredproductform_1,
        'featuredproductform_2': featuredproductform_2,
        'featuredproductform_3': featuredproductform_3,
    }
    
    return render(response, 'main/edit_home.html', context)