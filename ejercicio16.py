# Ejercicios del 16-20: Estructuras repetitivas (For)

# Ejercicio 16: Programa que realiza el conteo que se le pide

c=int(input("Ingrese el número desde el cuál le gustaría que comience a contar: "))
d=int(input("Ingrese el número hasta el cúal le gustaría que cuente: "))
e=int(input("Ingrese la razón a la que el conteo crece o decrece: "))
"""Usamos "for" comunmente para realizar un bucle limitado
    Dentro de range, el primer número es de donde comienza el conteo
    El segundo número determina el último número en contar, este será el anterior al que se digitó
    El tercer número indica la razón a la que crece o decrecen los número, se usan positivos o negativos"""
#Como escribimos d+1, el último número que podra contar será d, definido como entero.
for conteo in range(c,d+1,e):

    print (conteo)