
#Estructuras repetitivas (for) y contadores
# Ejercicio 22: Contando las veces que se trabaja variables, realizando bucles constantes y no constantes

import random

ntx=0
tx=0
n=int(input("Digite el número de ciclos que:  "))
for ciclo in range (n):
    print ("Se encuentra en el Ciclo Nº {} ".format(ciclo+1))
    x=random.randint(-5,10)
    print ("El valor aleatorio brindado es:  ",x)
    #Si el número es mayor que 0 se realiza dos listas de para multiplicar ignorando el número aleatorio obtenido
    if x>0:
        ntx+=1
        print ("*"*50)
        for i in range (1,5+1):
            for lm in range (5,10+1):
                multp=(f"{i} X {lm} = {lm*i} ")
                print (multp)
                
        print ("*"*50)
    #Si el número aleatorio es 0 no se llevará acabo ningun proceso
    elif x==0:
        print ("No puedes escribri si tu primera variable es 0")
        ntx+=1
    #Si no se cumple la condición se trabajará con el número aleatorio brindado
    else:
        tx+=1
        print ("*"*50)
        for y in range (-10,-4):
            asd=(f"{x} X {y} = {y*x} ")
            print (asd)
           
        print ("*"*50)
#Se acumula las veces que se trabaja o no trabaja la variable x 
print ("El Nº de veces trabajado con la variable \"x\" fue: {} ".format(tx))
print ("El Nº de veces que no se trabajó con la variable \"x\" fue : {} ".format(ntx))