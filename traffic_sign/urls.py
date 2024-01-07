"""crawer_information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from common import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('',views.login),
    path('index',views.index),
    path('personal',views.personal),
    path('get_result2/<pic_id>',views.get_result2),
    path('login_out',views.login_out),
    path('detection', views.detection),
    path('predict', views.predict),
    path('get_result/<pic_id>', views.get_result),
    path('get_pic', views.get_pic),
    path('pics', views.pics),
    path('del_pic', views.del_pic),
    path('predict2',views.predict2),
    path('detection2',views.detection2),
    path('computer',views.computer),
]
