from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from product.models import Product
from store_app.models import Categories, Contact_us

def BASE(request):
    return render(request,'Main/base.html')

def HOMEPAGE(request):
    product = Product.objects.filter(status ='Publish')

    context = {
        'product':product,
    }


    return render(request,'Main/index.html',context)
def SEARCH(request):
    query = request.GET.get('query')
    product = Product.objects.filter(name__icontains = query)

    context = {
        'product':product,
    }
    return render(request, 'Main/search.html',context)

def CONTACT(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

        contact = Contact_us(
            name = name,
            email = email,
            subject = subject,
            message = message,
        )

        subject = subject
        message = message
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from,['amit.luffy1@gmail.com'])
            contact.save()
            return redirect('homepage')
        except:
            return redirect('contact')
        
        


    return render(request, 'Main/contact.html')

def CART_DETAIL(request):
    return render(request,'Cart/cart_details.html')