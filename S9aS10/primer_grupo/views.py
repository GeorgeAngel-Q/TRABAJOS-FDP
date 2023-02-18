from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


#Vinculo para los homes
def home1 (request,*cadena,**cadenaId):
    return render (request,"home.html",{})
def home2 (request,*cadena,**cadenaId):
    return render (request,"home2.html",{})
def home3 (request,*cadena,**cadenaId):
    return render (request,"home3.html",{})


#Ejercicios for
def ejercicio_1 (request,*cadena,**cadenaId):
    j=3
    for i in range (0,10):
        if i!=0 or i!=5:
            j=j+1+i
        else:
            j=2
    return render (request,"ejercicio1.html",{'resultado':j})
def ejercicio_2 (request,*cadena,**cadenaId):
    k=3
    for m in range (0,8):
        if m!=2 and m!=3 and m!=5 and m!=7:
            k=k+m
        else:
            k=k+2
    return render (request,"ejercicio2.html",{'resultado': k})

def ejercicio_3 (request,*cadena,**cadenaId):
    a=["Enero","Febrero","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
    for i in [a]:
        a=random.choice(i) 
    return render (request,"ejercicio3.html",{'valor':a})

def ejercicio_4 (request,*cadena,**cadenaId):
    for numero in range(15,8,-2):
        numero=numero+0
    return render (request,"ejercicio4.html",{'numero':numero})

def ejercicio_5 (request,*cadena,**cadenaId):
    acum=0
    for i in ["Enero","Abril","Mayo","Junio","Agosto","Setiembre","Febrero",
              "Marzo","Abril","Mayo","Junio","Agosto","Setiembre","Octubre","Febrero","Marzo","Abril"]:
        acum+=1
    return render (request,"ejercicio5.html",{'valor':acum})


#Ejercicios while
def ejercicio_6 (request,*cadena,**cadenaId):
    p=float(10.5)
    n=5
    while p<=10.5:
        p=p+0.5*n
    return render (request,"ejercicio6.html",{'valor': p})

def ejercicio_7 (request,*cadena,**cadenaId):
    m=["si","no","tal vez"]
    i="no"
    acum=0
    while i!="si":
        i=random.choice(m)
        acum=acum+1
    return render (request,"ejercicio7.html",{'respuesta':acum})
def ejercicio_8 (request,*cadena,**cadenaId):
    n=300
    k=random.randint(2,5)
    while n>=287:
        n=n-k
    return render (request,"ejercicio8.html",{'valor':n})
def ejercicio_9 (request,*cadena,**cadenaId):
    car1=80
    car2=160
    d=car2-car1
    while d>0:
        car1=car1+1
        car2=car2-1
        d=car2-car1
    return render (request,"ejercicio9.html",{'valor':car1})
def ejercicio_10 (request,*cadena,**cadenaId):
    men=450
    women=250
    acum=0
    total=men+women

    while total>500:
        men=men-5
        women=women-5
        total=men+women
        acum=acum+1
    return render (request,"ejercicio10.html",{'valor':acum})


#Ejercicios Do while
def ejercicio_11 (request,*cadena,**cadenaId):
    k=["si","no"]
    dom="no"
    acum=0
    while True:
        if dom=="no":
            acum=acum+1
            dom=random.choice(k)
        else:
            break
    return render (request,"ejercicio11.html",{'valor':acum})
def ejercicio_12 (request,*cadena,**cadenaId):
    n=1
    ca=230
    que=210
    acum=0
    while True:
        if ca>130 and que>140:
            ca=ca-n*15
            que=que-n*13
            acum=acum+1
        else:
            acum=acum+1
            break
    return render (request,"ejercicio12.html",{'valor':acum})
def ejercicio_13 (request,*cadena,**cadenaId):
    prom=15
    cad=11
    while cad>10 and prom>10:
        cad=cad*3
        prom=prom/3
        total=cad+prom
    return render (request,"ejercicio13.html",{'valor': total})
def ejercicio_14 (request,*cadena,**cadenaId):
    m=15
    acum=0
    while True:
        l=random.randint(10,18)
        if m<l:
            m=m+3
            acum=acum+1
        elif m==l:
            m=m+1
            acum=acum+1
        else:
            break    
    return render (request,"ejercicio14.html",{'valor':acum})

def ejercicio_15 (request,*cadena,**cadenaId):
    x=0
    cont=0
    while True:
        x=x+1
        cont+=x
        if x==7:
            break
    return render (request,"ejercicio15.html",{'valor':cont})



