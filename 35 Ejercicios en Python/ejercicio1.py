#Ejercicios del 1-5: Estructuras secuenciales

#Ejercicio 1: Venta de producto X

#print: Para agregar textos, entre comillas. Para cademas "", o +str()+. Tambien se puede escribir dentro de ellas
print ("Venta de productos")
print ("Ingresar el nombre del producto")
nomprod=input()
#input: sirve para que se pueda escribir desde el teclado, es necesario dar en ENTER para que el programa continue
print ("Ingresar precio del producto")
pprod=input()
pprod=int(pprod)
#int: Para asignar a la variable la característica de número entero
print ("Ingresar la cantidad requerida del producto")
cantprod=input()
cantprod=int(cantprod)
# * : Operador matemático
prbr=pprod*cantprod

print ("El nombre del producto es:", nomprod)
print ("El precio del producto es:", pprod)
print ("La cantidad solicitada es:", cantprod)
print ("El precio bruto es:", prbr)


print ("Fin del sistema")