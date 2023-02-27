from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista_home (request,*cadena,**cadenaID):
    return render(request, "home.html",{})
def vista_home1 (request, *cadena, **cadenaID):
    return render (request, 'home1.html',{})
def vista_home2 (request, *cadena, **cadenaID):
    return render (request, "home2.html",{})