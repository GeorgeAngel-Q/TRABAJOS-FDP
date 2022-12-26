
#Acumuladores
# Ejercicio 28: Calculadora de potencias


num1=1
cant=0
quest="si"
print ("*"*20,"Calculadora de potencias","*"*20)
while num1!=0 and quest=="si":
    print ("-"*100)
    num1=float(input("Ingrese la base:  "))
    num2=int(input("Ingrese la potencia:  "))
    num3=num1**num2
    print ("{:.3f}".format(num3))
    cant=cant+1
    quest=input("¿Deseas repetir el proceso con otro número?")
    
print ("*"*100)
print ("Obtuviste {} respuestas en nuestro sistema".format(cant))
print ("!Vuelve pronto¡")
    