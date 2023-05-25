from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from product import product_views

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name = 'base'),
    path('',views.HOMEPAGE, name = 'homepage'),
    path('products/',product_views.PRODUCT, name ='products'),
    path('searchresult/',views.SEARCH, name = 'searchresult'),
    path('products/<str:id>',product_views.PRODUCTDETAIL, name='products'),
    path('contact/',views.CONTACT, name ='contact'),
    path('cart_details/',views.CART_DETAIL, name ='cart_details'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



