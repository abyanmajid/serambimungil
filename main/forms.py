from django import forms
from main.models import Home, About

# +-------------------+ EDIT HOME FORMS +-------------------+
home = Home.objects.get(id=1)

class MottoForm(forms.Form):
    motto = forms.CharField(label='Motto ', max_length=100, initial=home.motto)
    
class QualityForm_1(forms.Form):
    heading = forms.CharField(label='Heading ', max_length=100, initial=home.quality_1_heading)
    caption = forms.CharField(label='Caption ', max_length=100, initial=home.quality_1_caption)
    
class QualityForm_2(forms.Form):
    heading = forms.CharField(label='Heading ', max_length=100, initial=home.quality_2_heading)
    caption = forms.CharField(label='Caption ', max_length=100, initial=home.quality_2_caption)
    
class QualityForm_3(forms.Form):
    heading = forms.CharField(label='Heading ', max_length=100, initial=home.quality_3_heading)
    caption = forms.CharField(label='Caption ', max_length=100, initial=home.quality_3_caption)
    
class FeaturedProductForm_1(forms.Form):
    name = forms.CharField(label='Name ', max_length=100, initial=home.bestseller_1_name)
    caption = forms.CharField(label='Caption ', max_length=100, initial=home.bestseller_1_caption)
    description = forms.CharField(label='Description ', max_length=100, initial=home.bestseller_1_description)
    image = forms.ImageField(label='Image ', initial=home.bestseller_3_image, required=False)
    
class FeaturedProductForm_2(forms.Form):
    name = forms.CharField(label='Name ', max_length=100, initial=home.bestseller_2_name)
    caption = forms.CharField(label='Caption ', max_length=100, initial=home.bestseller_2_caption)
    description = forms.CharField(label='Description ', max_length=100, initial=home.bestseller_2_description)
    image = forms.ImageField(label='Image ', initial=home.bestseller_3_image, required=False)
    
class FeaturedProductForm_3(forms.Form):
    name = forms.CharField(label='Name ', max_length=100, initial=home.bestseller_3_name)
    caption = forms.CharField(label='Caption ', max_length=100, initial=home.bestseller_3_caption)
    description = forms.CharField(label='Description ', max_length=100, initial=home.bestseller_3_description)
    image = forms.ImageField(label='Image ', initial=home.bestseller_3_image, required=False)

# +-------------------+ EDIT MENU FORMS +-------------------+
class AddProductForm(forms.Form):
    product_name = forms.CharField(label='Name ', max_length=100)
    product_type = forms.CharField(label='Type ', max_length=100)
    product_description = forms.CharField(label='Description ', max_length=100)
    product_image = forms.ImageField(label='Image ', required=False)
    
class RemoveProductForm(forms.Form):
    product_id = forms.IntegerField(label='Product ID ')
    
# +-------------------+ ABOUT PAGE FORMS +-------------------+
about = About.objects.get(id=1)

class AboutForm(forms.Form):
    heading = forms.CharField(label='Heading ', max_length=100, initial=about.heading)
    body = forms.CharField(label='Body (up to 500 characters) ', max_length=250, widget=forms.Textarea, initial=about.body)