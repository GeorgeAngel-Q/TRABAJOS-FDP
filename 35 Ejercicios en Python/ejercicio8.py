
#Estructura selectiva doble
#Ejercicio 8: Sistema de atención médica básica

print ("Escriba su nombre, por favor: ")
name=input()

status=input("¿Necesita usted atención médica urgente?: ")
#Podemos crear varias variables e igualarlas, no solo podemos igualarlos con textos
m="si"
n="sí"
o="Si"
p="Sí"
#Haciendo uso de "if" para las condiciones y "or" para que de cualquier forma escrita acepte la orden
if status == m or status == n or status == o or status == p:
    print ("Dentro de unos instantes se le llamará para el recojo completo de sus datos y pueda ser atendido, por favor regrese a la sala de espera")
else:
    print ("Según lo informado, usted no necesita atención inmediata, si necesita información adicional acérquese a recepción")


print("Fin del sistema")