

# Ejercicio 15: Lista de pendientes en la semana

#Usando los condicionales
#\"abc\" es un comando que sirve para poner comillas dentro de print, también se puede con \'abc\'
print ("Lista de pendientes")
print ("")
print ("Escriba el día del que quiere ver los pendientes:")
day=input()
if day=="lunes":
    print (" 1. Limpiar el inodor")
    print (" 2. Limpiar el lavamanos")
    print (" 3. Juntar agua")
    print (" 4. Lavar ropa y tenderla")
elif day=="martes":
    print (" 1. Recoger la ropa" )
    print (" 2. Planchar la ropa")
    print (" 3. Guardar la ropa ")
    print (" 4. Estudiar para el examen")
elif day=="miercoles":
    print (" 1. Hacer la tarea de \"Fundamentos de Programación\" ")
    print (" 2. Presentar y exponer el proyecto de \"Tecnologías de la Información y Comunicación\"")
    print (" 3. Visitar a la abuela")
elif day=="jueves":
    print (" 1. Ver el partido de Aliados vs Gallinas")
    print (" 2. Bañar a los perros")
    print (" 3. Ir al mercado a hacer las compras")
elif day=="viernes":
    print (" 1. Completar la tarea de Cálculo Integral")
    print (" 2. Ayudar a mamá a cocinar")
    print (" 3. Salir con los amigos")
#\n: Para pasar a la siguiente linea 
else: 
    print ("Recuerda que: \n La lista esta diseñada desde el \"Lunes\" hasta el \"Viernes\"")