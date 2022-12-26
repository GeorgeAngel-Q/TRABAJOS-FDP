

#Ejercicio 4: Máquina que acumula el tiempo en segundos

#Haciendo uso del comando int para reconocer a las horas, minutos y segundos como números enteros
print ("Escriba el número de horas:")
hour=input()
hour=int(hour)

print ("Escriba el número de minutos:")
min=input()
min=int(min)

print ("Escriba el número de segundos:")
seg=input()
seg=int(seg)
#Haciendo uso de el operador matemático "*" y "+"
seg1=hour*3600
seg2=min*60

sum=seg+seg1+seg2
print ("El número total de segundos es:", sum)


print ("Fin del sistema")