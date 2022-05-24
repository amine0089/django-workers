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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import *

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('faq/', faq, name='faq'),
    path('contacts/', contact, name='contacts'),
    path('about-us/', about, name='about'),
    path('investments/', investments, name='investments'),
    path('past_projects/', past_projects, name='past_projects'),
    path('past_project/<str:name>', past_project, name='past_project'),
    path('investment/<str:name>', investment, name='investment'),
    path('investment_form/<str:invest>', investment_form, name='investment_form'),
    path('choose_payment/<int:invest>', choose_payment, name='choose_payment'),
    path('my_transactions/', my_transactions, name='my_transactions'),
    path('my_investments/', my_investments, name='my_investments'),
    path('delete_investment/<int:id>', delete_investment, name='delete_investment'),
    path('user_question/', question_through_email, name='question_through_email'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
