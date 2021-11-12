"""blogpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.http import HttpResponse

def foo(request):
    name= 'Internet Engineering Homework'
    html = "<html><body><h1>Project stack: Docker + Django + Nginx + HTTPS + Postgresql</h1><h2>by mojtaba_nafez</h2><h2>%s</h2></body></html>" % name
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', foo, name='index'),
]
