from math import prod
from django.http import Http404
from queue import PriorityQueue
from django.shortcuts import render
from main.models import Product, Home, About
from .forms import MottoForm, QualityForm_1, QualityForm_2, QualityForm_3, FeaturedProductForm_1, FeaturedProductForm_2, FeaturedProductForm_3, AddProductForm, RemoveProductForm, AboutForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
    about_page_details = About.objects.get(id=1)
    context = {
        'about_page_details': about_page_details
    }
    return render(response, 'main/about.html', context)

def contact(response):
    context = {}
    return render(response, 'main/contact.html', context)

# +-------------------------------+ EDIT PAGES +-------------------------------+
@login_required
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

@login_required
def edit_menu(response):
    if response.method == 'POST':
        # Retain Data
        addproductform = AddProductForm(response.POST)
        removeproductform = RemoveProductForm(response.POST)
        
        # ADD PRODUCT
        if addproductform.is_valid():
            product_name = addproductform.cleaned_data['product_name']
            product_type = addproductform.cleaned_data['product_type']
            product_description = addproductform.cleaned_data['product_name']
            product_image = addproductform.cleaned_data['product_image']
            Product.objects.create(
                product_name = product_name,
                product_type = product_type,
                product_description = product_description,
                product_image = product_image,
            )
            
            return HttpResponseRedirect('/menu/')
        
        # REMOVE PRODUCT
        elif removeproductform.is_valid():
            registered_product_ids = Product.objects.all().values_list('id', flat=True)
            entered_id = removeproductform.cleaned_data['product_id']
            
            if entered_id in registered_product_ids:
                Product.objects.get(id=entered_id).delete()
            return HttpResponseRedirect('/menu/')
        
    else:
        addproductform = AddProductForm()
        removeproductform = RemoveProductForm()

    context = {
        'addproductform': addproductform,
        'removeproductform': removeproductform,
    }
    return render(response, 'main/edit_menu.html', context)

@login_required
def edit_about(response):
    if response.method == 'POST':
        # Retain Data
        aboutform = AboutForm(response.POST)
        
        if aboutform.is_valid():
            # Apply Changes
            new_heading = aboutform.cleaned_data['heading']
            new_body = aboutform.cleaned_data['body']
            about = About.objects.get(id=1)
            about.heading = new_heading
            about.body = new_body
            about.save()
            
            return HttpResponseRedirect('/about/')
        
    else:
        aboutform = AboutForm()
    
    context = {
        'aboutform': aboutform
    }
    return render(response, 'main/edit_about.html', context)