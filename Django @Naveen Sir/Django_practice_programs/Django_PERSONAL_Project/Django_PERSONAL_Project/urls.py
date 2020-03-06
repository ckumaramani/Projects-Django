"""Django_PERSONAL_Project URL Configuration

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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Indexpage , name="gohomepage"),
    path('loginpage/', views.Loginpageopen, name="gologinpage"),
    path('registerlink/',views.Registerpageopen),
    path('Registrationsaved/', views.openLoginpage),
    path('Loginintouser/', views.gotoWelcomepage),
    path('logoutfromwelcomepage/', views.gotologinpagefromwelpage),
    path('viewallstaff/', views.viewallstaffDetails),
    path('Downloadallstaff/', views.Downloadalldetails),
    path('gohomepage/', views.gotohomepage1),
    path('gotobranchesI/', views.gotobranchesI, name="gobranchespage"),
    path('gotohomepageB/', views.GotohomepageB),
    path('gotoaboutusI/', views.GotoaboutusI, name="goaboutuspage"),
    path('gotocontactusI/', views.GotocontactusI, name="gocontactuspage")


]
