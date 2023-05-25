from typing import Iterable, Optional
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from store_app.models import Brand, Categories, Color, Filter_Price, Model_No

# Create your models here.
class Product(models.Model):
    STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
    STATUS = (('Publish','Publish'),('Draft','Draft'),)

    unique_id = models.CharField(unique=True,max_length=200,null =True,blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_images/img')
    price = models.IntegerField()
    information = RichTextField(null = True)
    description = RichTextField(null= True)
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.DateTimeField(default =timezone.now)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)
    model_no = models.ForeignKey(Model_No, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') +str(self.id)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return  self.name
    
class Images(models.Model):
    image = models.ImageField(upload_to='meida/Product_images/img')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


