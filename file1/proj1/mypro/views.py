from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return render(requests,'mypro/home.html')
def aboutus(requests):
    return render(requests,'mypro/about.html')

def hobbies(requests):
    return HttpResponse('<h2 > reading newspapers, listening music</h2>')