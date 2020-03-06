"""Project_CBV_MiniProject URL Configuration

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
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, FormView

from app import views
from app.forms import Register
from app.models import staff

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="homepage.html"),name="homepage"),
    path('Github/',RedirectView.as_view(url="https://github.com/ArjunMajeti"),name="Github"),
    path('enquiry/',TemplateView.as_view(template_name="Emquiry page.html"),name="enquiry"),
    path('login/', views.Loginpage.as_view(),name="login"),
    #path('login/',TemplateView.as_view(template_name="loginpage.html"),name="login"),
    path('branches/',TemplateView.as_view(template_name="branches.html"),name="branches"),
    path('aboutus/', views.Aboutus.as_view(),name="about us",),
    #path('aboutus/',TemplateView.as_view(template_name="about us.html"),name="about us"),
    path('contactus/',TemplateView.as_view(template_name="contact us.html"),name="contact us"),
    path('viewall/',ListView.as_view(template_name="viewall.html", model=staff),name="viewall"),
    path('viewallid/',ListView.as_view(template_name="viewallid.html", model=staff),name="viewallid"),
    path('vieweach<int:pk>/',DetailView.as_view(template_name="vieweach.html",model=staff),name="vieweach"),
    path('register/',views.Register.as_view(),name="register"),
    path('home/', TemplateView.as_view(template_name="Home.html"))

]

