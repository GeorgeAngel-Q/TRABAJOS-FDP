#Ejercicios del 6-10: Estructuras selectivas simple, doble y múltiple
#Estructura selectiva simple
#Ejercicio 6: Recomendación en caso de estar hambriento

"""
IF: Es el condicional que permite seguir un proceso o desviar el proceso, en caso de no cumplirse la condicion
Para agregar condiciones debemos poner la variable y hacer uso de "==" para dar valores, no olvidar los ":" al final
La primera forma de agregar otra condición es con "and" para que se deban cumplir las dos
La segunda forma de agregar otra condicion es con "or", ahora será necesario que se cumpla al menos una de ellas
Las dos ultimas líneas haciendo uso de la lógica proposicional
"""

hambre=input("¿Está usted hambriento? ")
if hambre== "Sí" or hambre== "Si" or hambre== "sí" or hambre== "si":
    print ("Recuerde que comer a deshoras puede causar problemas, alimentese adecuadamente")


print ("Fin del sistema")