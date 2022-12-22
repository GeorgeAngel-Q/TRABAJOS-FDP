

#Ejercicio 5: Sistema administrativo de ganancias de la empresa

print ("Bienvenido al sistema administrativo de la empresa Sidjan S.A.")
#float: Asignar la característica de número real al dígito ingresado
Iab=float(input("Registre el ingreso que se dio el mes de Abril: "))
Ima=float(input("Registre el ingreso que se dio el mes de Mayo: "))
Iju=float(input("Registre el ingreso que se dio el mes de Junio: "))

#Seguimos haciendo uso de operadores matemáticos básicos
sum1 = Iab + Ima + Iju

Eab=float(input("Registre el egreso que se dio el mes de Abril: "))
Ema=float(input("Registre el egreso que se dio el mes de Mayo: "))
Eju=float(input("Registre el egreso que se dio el mes de Junio: "))


sum2 = Eab + Ema + Eju


print ("El ingreso bruto es: ",sum1)
print ("El egreso bruto es: ", sum2)


Gan=sum1-sum2

print ("Las ganacias que se lograron en la empresa son:", Gan)
