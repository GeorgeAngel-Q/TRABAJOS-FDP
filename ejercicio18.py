

# Ejercicio 18: Activar bomba para demoler un edificio en ruinas

#Import time: usaremos "sleep", nos permite hacer el conteo más rápido o más lento, tiempo de intervalo
import os
import time

print ("Asistente de activación de la bomba")
print ("Tiempo estimado para la detonación desde su pulso: 12 segundos")
input("Para inciar el conteo regresivo pulsa la tecla ENTER")
#Cuenta regresiva de 1 en 1 desde 12 hasta 0
for numero in range(12,-1,-1):
    print (numero)
    time.sleep(0.5)
    os.system('cls')

print ("El edificio ha sido demolido con éxito")