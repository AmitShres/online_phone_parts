from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return  self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return  self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):
        return  self.name

class Filter_Price(models.Model):
    FILTER_PRICE = {
        ('100 to 5000','100 to 5000'),
        ('5000 to 10000','5000 to 10000'),
        ('10000 to 15000','10000 to 15000'),
        ('15000 to 20000','15000 to 20000'),
        ('20000 to 30000','20000 to 30000'),
    }
    price = models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return  self.price

class Model_No(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return  self.name

class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



