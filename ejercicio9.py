
#Estructura selectiva múltiple
#Ejercicio 9: Comparativo de una semidiferencia con un número aleatorio

print ("Ingresar un primer número: ")
num1=input()
num1=int(num1)

print ("Ingrese un segundo número: ")
num2=input()
num2=int(num2)

smdf=(num1-num2)/2
#Usando random. También se puede usar "import random" y luego "ra=random.randint()"
#Existen varias formas de sacar números aleatorios: randint, randrange, random, uniform.
#Una forma para hacer lo mismo en listas es: choice
from random import randint
ra=randint(34,387)
#str: Permite unir textos con números mediante cadenas
""" if: Agregar una condición
    elif: Agregar otra condición diferente a la principal, esta es opcional
    else: Niega las otras condiciones agregadas, esta es la última que lee el sistema
"""
if smdf < ra:
    print ("La semidiferencia de los dos números es, " + str(smdf) + ", el cual es menor que", ra)
elif smdf == ra:
    print ("La semidiferencia es " + str(smdf) + ", el cual es igual al número que se obutvo aleatoriamente: ",ra)
else:
    print ("La semidiferencia de los dos números es, " + str(smdf) + ", el cual es mayor que", ra)


print ("Fin del sistema")
