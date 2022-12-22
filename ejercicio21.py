# Ejercicios del 21-25: Estructuras repetitivas (for), acumuladores y contadores
#Estructuras repetitivas (for), acumuladores y contadores
# Ejercicio 21: Acumulador y contador de múltiplos de 3

import os

ve=int(input("Digite la cantidad de ciclos que desea realizar:  "))
cont=0
acum=0
# El usuario tiene el poder de elegir cuantos ciclos desea realizar
for i in range(ve):
    print ("***** Ciclo Nº" + str(i+1) + "*****")
    x=int(input("Digite un número:  "))
    # Haciendo uso de %n==x, para que se cumpla la condición. También se pudo usar x %3 != 0
    #La condición es que exista residuo para que no me permita usar el sistema
    if x%3==1 or x%3==2:
        print ("")
        print ("Digite solo múltiplos de 3")
    #La negación de esta me dice que acá se registran, acumulan y cuentan los múltiplos de 3
    else:
        """Contadores: Para agregar de 1 en 1. se puede de dos formas con+=1 o cont=cont+1
           Acumuladores: Puede ir sumando los valores que se agregan. Se puede de dos formas acum+=x o acum=acum+x"""
        cont+=1
        acum+=x
    print ("")
    print ("La cantidad de números que son múltiplos de 3 es: ", cont)
    print ("La acumulación de números que son múltiplos de 3 es: ",acum)
    print ("")
    input ("Presione ENTER para continuar")
    os.system ('cls')
print ("La cantidad de números que son múltiplos de 3 usados fueron: ",cont)
print ("La suma de todos los múltiplos de 3 usados fue: ",acum)