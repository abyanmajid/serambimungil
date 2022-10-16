from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_type = models.CharField(max_length=25)
    product_description = models.CharField(max_length=250)
    product_image = models.ImageField(null=True, blank=True, upload_to='images/')
    
    def __str__(self):
        return self.product_name