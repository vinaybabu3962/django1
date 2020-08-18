from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
   return HttpResponse('<h1>This is my page</h1>')
def about(requests):
    return HttpResponse('<h1>Iam Vinay from Vasavi IT b</h1>')
def hobbies(requests):
    return HttpResponse('<h2 style="color:red"> reading newspapers, listening music</h2>'