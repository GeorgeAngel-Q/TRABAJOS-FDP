

# Ejercicio 13: Desarrollo de problema matemático

"""Import math: Librería matemática, usaremos square root "sqrt" para la raíz cuadrada
   Import os: Libería os, usaremos os.system('cls'), cls=clear screen
   Import random: Librería random, usaremos radint para números aleatorios
"""
import math
import os
import random

a= float(input("Ingrese la altura del edificio A: "))
b= float(input("Ingrese la altura del edificio B: "))
c= random.randint(1,100)

print ("")
print ("En un edificio el edificio A se tiene " + str(a) + " metros de altura y se tiene el edificio B con altura de " + str(b) + " metros. Además de estar separados por una distancia de " + str(c) + " metros. Se solicita encontrar la medida de la distancia entre las partes más altas de ambos edificios")
input ("Presione ENTER para ver la solución")
#os.system('cls'): Borrará de la pantalla lo que hayamos realizado, el proceso sigue estando registrado pero no lo vemos.
os.system('cls')
#Haciendo uso de math.sqrt para sacar la raíz cuadrada 
di1= math.sqrt((a-b)**2 + c**2)
di2= math.sqrt((b-a)**2 + c**2)              

#Definiendo condicionales ya que trabajamos con reales y es necesario que el resultado de la raiz se >= 0
if a>b:
    print ("La altura del edificio A es: ",a)
    print ("La altura del edificio B es: ",b)
    print ("La distancia horizontal que los separa es: ",c)
    print("")
    print ("SOLUCIÓN: ")
    print ("1.Restar las alturas de los edificios: ",a-b)
    print ("2.Aplicar el teorema de pitágoras usando el dato obtenido y el dato brindado")
    print ("3.Operar ")
    print ("")
    print ("RESPUESTA: ")
    print ("La distancia de los tejados entre ambos adificios es: ",di1)
elif a==b:
    print ("La distancia de los tejados entre ambos edificios es: ",c)
else:
    print ("La altura del edificio A es: ",a)
    print ("La altura del edificio B es: ",b)
    print ("La distancia horizontal que los separa es: ",c)
    print ("")
    print ("SOLUCIÓN: ")
    print ("1.Restar las alturas de los edificios: ",b-a)
    print ("2.Aplicar el teorema de pitágoras usando el dato obtenido y el dato brindado")
    print ("3.Operar ")
    print ("")
    print ("RESPUESTA")
    print ("La distancia de los tejados entre ambos adificios es: ",di2)



