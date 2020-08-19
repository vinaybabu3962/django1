from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns = [
    url(r'contactname.*', views.contactname, name='contactname'),
    url(r'contactnumber.*', views.contactnumber, name='contactnumber'),
]