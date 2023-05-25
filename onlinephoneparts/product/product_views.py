from django.shortcuts import render, redirect

from product.models import Product
from store_app.models import Brand, Categories, Color, Filter_Price

# Create your views here.
def PRODUCT(request):
    product = Product.objects.filter(status ='Publish')
    categories = Categories.objects.all()
    brand = Brand.objects.all()
    color = Color.objects.all()
    price_filter = Filter_Price.objects.all()

    CatId = request.GET.get('categories')
    Filter_Id = request.GET.get('price_filter')
    ColorId = request.GET.get('color')
    BrandId = request.GET.get('brand')
    ATOZId = request.GET.get('ATOZ')
    ZTOAId = request.GET.get('ZTOA')
    LTOHId = request.GET.get('LTOH')
    HTOLId = request.GET.get('HTOL')

    if CatId:
        product = Product.objects.filter(categories= CatId ,status ='Publish')
    elif Filter_Id:
        product = Product.objects.filter(filter_price= Filter_Id ,status ='Publish') 
    elif ColorId:
        product = Product.objects.filter(color= ColorId ,status ='Publish') 
    elif BrandId:
        product = Product.objects.filter(brand= BrandId ,status ='Publish')  
    elif ATOZId:
        product = Product.objects.filter(status ='Publish').order_by('name')
    elif ZTOAId:
        product = Product.objects.filter(status ='Publish').order_by('-name')
    elif LTOHId:
        product = Product.objects.filter(status ='Publish').order_by('price')
    elif HTOLId:
        product = Product.objects.filter(status ='Publish').order_by('-price')   
    else:
        product = Product.objects.filter(status ='Publish')
    context = {
        'product':product,
        'categories':categories,
        'brand':brand,
        'color':color,
        'price_filter':price_filter,
    }

    return render(request, 'Main/product.html',context)

def PRODUCTDETAIL(request,id):
    prod = Product.objects.filter(id=id).first()

    context ={
        'prod':prod,
    }
    return render(request,'Main/singleproduct.html',context)