from django.shortcuts import render , HttpResponse

# Create your views here.
def  returnHello(requset):
    return HttpResponse("<h1>Hello World Saleh Taerian</h1>")