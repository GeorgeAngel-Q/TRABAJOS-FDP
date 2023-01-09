#Apuesta virtual
from datetime import datetime
import random
billetera=10
win=0
lose=0
acierto=3
desacierto=2
resp="si"
print ("Bienvenida a tu sitio de apuesta \"Prograbet\"")
print ("Nuevo inicio de sesión: {}".format(datetime.now()))
print ("Su saldo actual es de {} $".format(billetera))
quest=input("¿Desea apostar? ")
while resp=="si" and billetera>2 and quest=="si":
    lista1=["Perú","Chile"]
    lista2=["Bolivia","Argentina"]
    x=random.randint(0,1)
    z=random.randint(0,1)
    c=random.choice(lista1)
    d=random.choice(lista2)
    print ("El partido que se llevará a cabo hoy es entre {} y {}".format(c,d))

    marc1=int((input("Ingrese los goles a favor de {}: ".format(c))))
    marc2=int((input("Ingrese los goles a favor de {}: ".format(d))))
    print ("El marcador resultante de este partido entre {} y {} es: {} - {}".format(c,d,x,z))
    if billetera>2:
        if marc1==x and marc2==z and resp=="si":
                print ("Felicidades usted acertó")
                win+=1
                billetera+=acierto
                print ("Su saldo actual es {}".format(billetera))
                resp=input("¿Desea volver a jugar?")
        else:
                print ("Desafortunadamente usted perdió")
                lose+=1
                billetera=billetera-desacierto
                print ("Su saldo actual es {}".format(billetera))
                resp=input("¿Desea volver a jugar?")
print ("El número de aciertos en esta sesión fue: {}".format(win))
print ("El número de desaciertos en esta sesión fue: {}".format(lose))
print ("La cantidad final de dolares en su billetera es: {}".format(billetera))
