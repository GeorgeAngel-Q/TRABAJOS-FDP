
#Estructura selectiva doble
#Ejercicio 7: Comprobar si un número es par

print ("Ingrese un número: ")
num=input()
num=int(num)
#Haciendo uso del if creamos una condición para que se ejecute, de lo contrario usamos else para la negación
"""Existen varias formas de sacar que un número es múltiplo de otro la primera es la que utilizo acá
La doble barra significa división aproximada, no muestra decimales, siempre es exacta y redondea al entero más bajo 
Algo similar a lo que haría math.floor(), ejem:  5//2=2
La barra normal indica división común con decimal, ejem: 5/2=2.5
Al igualarlos puedes obtener una verdad o una falsedad, ahi entra if a hacer respetar la condición
"""
if num //2 == num/2:
    print ("El número " + str(num) +", es par")
else:
    print ("El número " + str(num) + ", es impar")


print ("Fin del sistema")


