
#Ejercicio 2: Almacén de maquinarias pesadas

print ("Bienvenido al sistema de Almacén maquinarias pesadas")
print ("Recuerde que la capacidad máxima de maquinarias es 250 unidades, en caso de sobrepasar dicha cantidad no podrá almacenar su maquinaria")
print ("Ingrese la cantidad a depositar")
cantdep=input()
cantdep=int(cantdep)
#desde librería random importar módulo randint, sirve para que la máquina genere números aleatorios
from random import randint
cantact=randint(100,250)
cantbr=cantdep+cantact
print ("La cantidad actual de maquinaria es:", cantact)
print ("La cantidad que quiere depositar es:", cantdep)
print ("El total de maquinarias sería:", cantbr)


print ("Fin del sistema")