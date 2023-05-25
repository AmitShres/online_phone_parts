from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/' , register_attempt , name="register_attempt"),
    path('login/' , login_attempt , name="login_attempt"),
    path('token_send/' , token_send , name="token_send"),
    path('success/' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error/' , error_page , name="error"),
    path('logout/',logout_attempt,name="logout_attempt"),   
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
