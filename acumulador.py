
# Punto 2 de DEMO EXAMEN PARCIAL

print ("Digite la cantidad de datos que desea ingresar")
n=int(input())
acum=1
for i in range(n):
    print("***Ingrese el dato ",str(i+1),"***") 
    x=float(input())
    acum+=x
prom=acum/n
print ("El promedio de la acumulación de los datos es ",prom)

