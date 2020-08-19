from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator
def contactname(requests):
    return HttpResponse('name of contact 1 is k.vinay babu')
def contactnumber(requests):
    return HttpResponse('phone number of contact 1 is 9573707043')
    