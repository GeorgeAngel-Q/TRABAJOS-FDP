
#Estructura selectiva múltiple
#Ejercicio 10: Comparativo entre promedio y dos números cualquiera

print ("Ingresar un primer número: ")
num1=input()
num1=int(num1)

print ("Ingrese un segundo número: ")
num2=input()
num2=int(num2)

prom=(num1+num2)/2
#Haciendo uso de "and", será necesario que se cumplan ambas condiciones 
if prom < 30 and prom > 10:
    print ("El promedio de los números ingresados es " +  str(prom)  + ", el cual es menor que 30, pero mayor que 10")
elif prom ==30:
    print ("El promedio de los números ingresados es " +  str(prom)  + ", el cual es mayor que 10")
elif prom ==10:
    print ("El promedio de los números ingresados es " +  str(prom)  + ", el cual es menor que 30")
else:
    print ("El promedio de los números ingresados es " +  str(prom)  + ", el cual es menor que 10 o mayor que 30")
  
    
print ("Fin del sistema")