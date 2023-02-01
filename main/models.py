from itertools import product
from django.db import models
from PIL import Image

class Home(models.Model):
    # Motto
    motto = models.CharField(max_length=100, null=True)
    
    # Qualities
    quality_1_heading = models.CharField(max_length=50, null=True)
    quality_1_caption = models.CharField(max_length=100, null=True)
    
    quality_2_heading = models.CharField(max_length=50, null=True)
    quality_2_caption = models.CharField(max_length=100, null=True)
    
    quality_3_heading = models.CharField(max_length=50, null=True)
    quality_3_caption = models.CharField(max_length=100, null=True)
    
    # Best Sellers
    bestseller_1_name = models.CharField(max_length=50, null=True)
    bestseller_1_caption = models.CharField(max_length=50, null=True)
    bestseller_1_description = models.CharField(max_length=250, null=True)
    bestseller_1_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    bestseller_2_name = models.CharField(max_length=50, null=True)
    bestseller_2_caption = models.CharField(max_length=50, null=True)
    bestseller_2_description = models.CharField(max_length=250, null=True)
    bestseller_2_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    bestseller_3_name = models.CharField(max_length=50, null=True)
    bestseller_3_caption = models.CharField(max_length=50, null=True)
    bestseller_3_description = models.CharField(max_length=250, null=True)
    bestseller_3_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    def __str__(self):
        return "Home Page"

class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_type = models.CharField(max_length=25)
    product_description = models.CharField(max_length=250)
    product_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.product_image:
            img = Image.open(self.product_image.path)
            
            if img.width > 600 or img.height > 450 or img.width < 600 or img.height < 450:
                output_size = (600, 450)
                img.thumbnail(output_size)
            
            img.save(self.product_image.path)