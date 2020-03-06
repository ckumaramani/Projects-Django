"""Project36_CBV_V_TeV_listView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from app36 import views
from django.views.generic import TemplateView, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name="Index.html"), name="index"),
    path('Branches/', views.TemplateView.as_view(template_name="Branches.html"), name="branches"),
    path('login/', views.TemplateView.as_view(template_name="login.html"), name="login"),
    path('aboutus/', views.TemplateView.as_view(template_name="Aboutus.html"), name="aboutus"),
    


]
