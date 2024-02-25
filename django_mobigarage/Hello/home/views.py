from django.shortcuts import render, HttpResponse
# import pandas as pd
# import os
# from templates import *


#rendering template
def mini_site(request):
    context = {
        "variable":"phones and accessories"
        }
    return render(request,"mini_site.html",context)

def base(request):
    return render(request,"base.html")

#take the user to about_us.txt document after clicking on about us button
def about_us(request):
    return render(request,"about_us.txt")

#take the user to rating.html document
def rating(request):
    return render(request, "rating.html")

def price(request):
    return render(request,'price.html')
    
def brand(request):
    return render(request,"brands.html")

#Create your views here.
def default(request):
    return HttpResponse("THIS IS HOMEPAGE OF WEBSITE")

def about(request):
    return HttpResponse("This is the about page.")


