"""solomartel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('activate_account/', activate_account, name='activate_account'),
    path('reset_password/', reset_password, name='reset_password'),
    path('user_profile/', user_profile, name='user_profile'),
    path('update_personal_data/', update_personal_data, name='update_personal_data'),
    path('update_address_data/', update_address_data, name='update_address_data'),
    path('update_bank_data/', update_bank_data, name='update_bank_data'),
    path('change_password/', change_password, name='change_password'),
    path('send_promotion/', home_mail_sending, name='send_mail'),
    path('logout/', logout, name='logout'),
    path('get/ajax/validate/user_name/', check_user_name, name='check_user_name'),
    path('get/ajax/validate/email_user/', check_email_user, name='check_email_user')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
