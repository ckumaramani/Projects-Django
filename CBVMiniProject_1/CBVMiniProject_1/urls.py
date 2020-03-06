"""CBVMiniProject_1 URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView

from CBVMiniProject_1 import settings
from app import views
from app.models import Employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="Homepage.html"), name="homepage"),
    path('loginpage/',TemplateView.as_view(template_name="loginpage.html"),name="loginpage"),
    path('Aboutuspage/',TemplateView.as_view(template_name="feedbackform.html"),name="Aboutuspage"),
    path('Contactus/', TemplateView.as_view(template_name="contactus.html"),name="contactus"),
    path('Companyinfo/', TemplateView.as_view(template_name="Companyinfo.html"),name="Companyinfo"),
    path('Gallery/', TemplateView.as_view(template_name="Gallery.html"),name="Gallery"),
    path('Achivements/', TemplateView.as_view(template_name="Achivements.html"),name="Achivements"),
    path('register/',views.Register),
    path('Save/',views.Save),
    path('Enquirypage/',views.Enquirypage.as_view(),name="Enquirypage"),
    #path('registered/', ListView.as_view(template_name="ViewAll")),
    path('AdminLoginpage/',views.AdminLoginPage),
    path('AdminValidations/', views.AdminLoginValidations),
    path('logout/', views.Logout),
    #Viewall
    path('viewall/',views.Viewall),
    path('EmployeeLoginPage/',views.EmployeeLoginpage),
    #Employee Welcome Page
    path('EmployeeWelcomePage/',views.EmployeeWelcomePage),
    path('update<int:pk>/', views.update.as_view()),
    path('delete<int:pk>/', views.Delete.as_view())
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
