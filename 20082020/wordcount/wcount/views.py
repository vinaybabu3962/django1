from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def home(requests):
    return render(requests,'wcount/home.html')
def count(requests):
    mytext=requests.GET['fulltext']
    wcount1=mytext.split()
    wcount=len(wcount1)
    f=[]
    for i in wcount1:
        if i in f:
            continue
        else:
            f.append(i)
    str1=""
    for i in f:
        str1=str1+i+str(wcount1.count(i))
        str1+='\n'
    
        
    
    return render(requests,'wcount/count.html',{'mycount':wcount,'ourlist':str1})