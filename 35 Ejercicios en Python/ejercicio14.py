

# Ejercicio 14: Porcentajes destinados a un área, respecto al monto

print ("En una clínica existen tres áreas: Ginecología, Radiologia y Cirugia. El presupuesto anual de la clínica se reparte conforme a la siguiente tabla")
print ("")
print ("Área            Porcentaje de Presupuesto")
print ("Cirugia                   27%")
print ("Radiología                35%")
print ("Ginecología               38%")
print ("")
print ("Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal")
print ("")
#Haciendo uso de float y operadores aritméticos
mon=float(input("Ingrese el monto anual:  "))

cir=0.27*mon
rad=0.35*mon
gin=0.38*mon

print ("El área de Cirugia recibirá:  ",cir)
print ("El área de Radiología recibirá:  ",rad)
print ("El área de Ginecología recibirá:  ",gin)
