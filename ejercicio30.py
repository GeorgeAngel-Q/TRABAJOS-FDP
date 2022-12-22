
#Estructuras repetitivas (while), acumuladores y contadores
# Ejercicio 30: Sitio de apuesta Virtual (Copa América)
import random
from datetime import datetime
"""Importamos la libreria random, ya que estamos en un sitio en el que se usa probabilidades 
   Definimos las variables necesarias para que nuestro juego siga la lógica
   Daremmos la bienvenida respectiva y despues de responder la pregunta podremos iniciar el juego
   Además haremos uso de .format para insertar las variables, para no estar colocando cada rato "str". """
acierto=3
desacierto=2
cont="si"

gana=0
pierde=0
saldo=10
date=datetime.now()

print ("Bienvenido a \"Prograbet\" tu sitio de apuestas")
print ("Nuevo inicio de sesión registrado:  {}".format(date))
print ("Usted cuenta con ${} de saldo en su tarjeta".format (saldo))
print ("")
print ("-"*70)
print ("NOTA: \n Por cada acierto se le otorga 3$ \n Por cada desacierto se le resta 2$ de su saldo")
print ("-"*70)
apuesta=input("¿Desea apostar?: ")
print ("")
"""Usaremos while para que nuestro juego pueda repetirse indefinidamente hasta que el usuario ya no quiera
   jugar o se le agote el saldo que es necesario para poder seguir apostando
   Usamos "Apuesta=si" para que el juego pueda correr desde la primera vez
   Elaboramos la lista correspondiente de paises separados por grupos para poder sacar algunos aleatoriamente
   la lista aleatoria la pongo dentro para que al repetirse el bucle salgan valores diferentes cada vez"""
while saldo>=3 and cont=="si" and apuesta=="si":

    lista1=["Argentina", "Chile", "Perú", "Colombia"]
    lista2=["Bolivia","Uruguay", "Paraguay","Ecuador"]

    x=random.choice(lista1)
    y=random.choice(lista2)
    z=random.randint(0,1)
    a=random.randint(0,1)

    print ("Hoy se lleva a cabo el partido de {} y {}".format(x,y))
    """Acá definiremos las condiciones necesarias para que el juego tenga sentido haciendo uso de if para que 
    se ejecute siempre y cuando nuestro saldo sea mayor o igual que 3 y que la variable con sea "si", 
    la primera vez se ejecutará con normalidad, ya que lo definimos con anterioridad en la linea 12"""
    if cont=="si" and saldo>=3:
        marc1=int(input("Ingrese la cantidad de goles que usted considere a favor de {}: ".format(x)))
        marc2=int(input("Ingrese la cantidad de goles que usted considere a favor de {}: ".format(y)))
        print("El resultado del partido es: {} - {}".format(z,a))
        print ("Usted predijo que el partido de {} y {} sería: {} - {}".format(x,y,marc1,marc2))
        #Abrimos otra condicional en caso de que acertemos, se sumará a nuestro saldo los $3 y se contará el acierto
        if marc1==z and marc2==a:
                print ("")
                print ("Felicidades usted ganó")
                saldo+=acierto
                gana+=1
                print ("Su saldo actual es: {}".format(saldo))
                cont=input("¿Desea apostar por otro partido?: ")
                print ("*"*70)
        #En caso de que no acertemos se nos descontará $2 de nuestro saldo, también se contará el desacierto 
        else:
            print("")
            print ("Desafortunadamente usted perdió")
            saldo-=desacierto
            pierde+=1
            print ("Su saldo actual es: {}".format(saldo))
            #En caso de que el saldo no sea suficiente no será necesario que nos den la opción de seguir jugando
            if saldo>=3:
                cont=input("¿Desea apostar por otro partido?: ")
                print ("*"*70)
#No hago uso else para el primer if ya que se cerrará solo en caso de que no cumpla las condiciones de while
#Finalmente nos mostrarán las estadísticas del juego de hoy            
        
print ("Usted acertó {} partidos".format(gana))
print ("Usted desacertó {} partidos".format(pierde))
print ("Usted cuenta con un saldo final de: {}".format(saldo))
print ("¡Gracias por jugar!")
print("-"*70)
print ("NOTA: \n Si usted desea seguir jugando y no le queda saldo puede recargarlo desde nuestra página web")
