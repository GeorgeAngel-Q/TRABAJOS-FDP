

# Ejercicio 20: Tabla de multiplicar del 11-20

import os
# Para num en rango (11,21), nos servirá poner los números o el hasta que número vamos a multiplicar 
for num in range(11,21):
    # f : Otra forma de añadir cadenas, strings.
    print (f'Tabla del número {num}')
    #Definimos el segundo bucle por el cual se multiplicará, tambien puede ser range (1,11), el último no se cuenta
    for multiplicador in range(1,10+1):
        print (f'{multiplicador} X {num}= {multiplicador*num}')

    input("Presione la tecla ENTER para avanzar a la siguiente tabla")
    os.system('cls')

print ("Fin del sistema")