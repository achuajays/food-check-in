"""food_qu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path , include 
from food_qu_ch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('food_qu_ch.urls')),
    path('',views.login,name="login"),
    # path('delete/<int:row_id>/', views.delete_row_view, name='delete_row'),
    path('reg/',views.registration,name="registration"),
    path('ver/',views.verification,name="verification"),
    path('fod/',views.foodpage,name="foodpage"),
    path('reglog/',views.register,name="register"),
    path('main/',views.main,name="main"),
    path('loginver/',views.loginver,name="loginver"),

]
