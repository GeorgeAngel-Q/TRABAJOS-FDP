# Ejercicios del 26-30: Estructuras repetitivas (while), acumuladores y contadores
# Estructura repetitiva while 
# Ejercicio 26: Convertidor de Grados Celsius a Farenheit y Kelvin

import os
#While: Bucles indefinidos con True, restringidos con condicionales para romperlos usamos break y no accesibles con False
while False:

    print ("Convertidor de Grados Celsius a Farenheit y Kelvin")
    print ("")
    print ("Seleccione un opción: ")
    print (" 1. De Celsius a Kelvin")
    print (" 2. De Celsius a Farenheit")
    print (" 3. Salir del sistema")
    
    el=int(input())

    if el==1:

     c1= int(input("Determine el número de grados Celsius:  "))
     k= c1 + 273

     print ("La conversión de " + str(c1) + " grados Celsius resulta en " + str(k) + " grados Kelvin")
     input ("Presione ENTER para inciar una nueva conversión")
     print("")
     print("")

     os.system('cls')

    elif el==2:
     q= int(input("Determine el número de grados Celsius:  "))
     f= q*9/5 + 32

     print ("La conversión de " + str(q) + " grados Celsius resulta en " + str(f) + " grados Farenheit")
     input ("Presione ENTER para inciar una nueva conversión")
     print("")
     print("")
     os.system('cls')
    
    elif el==3:
     print ("Sesión Finalizada")
    
    else:
     input ("ERROR, vuelve a intentarlo pulsando ENTER")
     os.system('cls')

    if el==3:
        break


