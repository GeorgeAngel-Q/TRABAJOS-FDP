

# Ejercicio 19: Pares e impares cercanos al dígito ingresado

print ("Ingrese un número: ")
num=input()
num=int(num)
# Definimos las variables que se usarán posteriormente
a= num + 2
b= num + 4
c= num + 6
d= num + 8
e= num + 10

f= num - 2
g= num - 4
h= num - 6
i= num - 8
j= num - 10

# %n==0 : Realiza la divisón y arroja el residuo de esta
if num % 2 == 0:
    print ("El número " + str(num) +", es par")
    print ("El sistema escribirá los 5 números pares siguientes")
    #Para mostrar la lista de los siguientes números
    for rest in [a,b,c,d,e,]:
        print (rest)
        
else:
    print ("El número " + str(num) + ", es impar")
    print ("El sistema escribirá los 5 números impares anteriores")
    #Para mostrar los números anteriores
    for rent in [f,g,h,i,j]:
        print (rent)


print ("Fin del sistema")