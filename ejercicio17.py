

# Ejercicio 17: Programa que imprime nombres de forma vertical

name1=input("Escriba su primer nombre: ")
name2=input("Escriba su segundo nombre: ")
lastname1=input("Escriba su primer apellido: ")
lastname2=input("Escriba su segundo apellido: ")
print ("Se mostraran sus nombres completos de forma vertical")
"""
Sustituimos range por una lista en corchetes, por defecto se imprime la lista en vertical
Si deseamos imprimir la lista en horizontal y unida, puede usarse en números 
para ello se escribirá end="" 
"""
for nomcom in [name1,name2,lastname1,lastname2]:
        print (nomcom)
