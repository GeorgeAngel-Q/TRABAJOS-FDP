
#Estructura repetitiva while
# Ejercicio 27: Libro de reclamaciones virtual
import os
name="El gato cusqueño"
print ("Bienvenido al Libro de Reclamaciones Virtual de",name)
print ("")

while True:
    print( "Por favor, seleccione el motivo de su reclamo")
    print ("")
    print (" 1. Faltas de respeto")
    print (" 2. Demora excesiva en la atención")
    print (" 3. Los SS.HH. estan en mal estado")
    print (" 4. Otro")
    print (" 5. Salir del sistema")

    mot=int(input())
    if mot==1:
        print ("Lamentamos las molestias ocasionadas hacia su persona, por favor rellene lo solicitado")
        input ("Sede del restaurante: ")
        input ("Fecha del incidente: ")
        input ("Hora del incidente: ")
        input ("Nombre del encargado de su atención: ")
        input ("Puede agregar un comentario: ")
        print ("")
        print ("Su reclamo se ha registrado correctamente")
        input ("Pulse ENTER para regresar al menú")
        os.system('cls')
    elif mot==2:
        input ("Sede del restaurante: ")
        input ("Hora del incidente: ")
        input ("Puede agregar un comentario: ")
        print ("")
        print ("Su reclamo ha sido registrado correctamente")
        input ("Pulse ENTER para regresar al menú")
        os.system('cls')

    elif mot==3:
        print ("Por favor, elabore una lista de lo que considere en malas condiciones de los Servicios Higiénicos")
        print ("Para iniciar escriba INICIO")
        print ("Para finalizar escriba FIN")
        x=input()

        while x=="INICIO" or x=="FIN":
         if x=="INICIO":
            m=input()
            if m=="FIN":
             print ("Lista Finalizada")
             break      

         elif x=="FIN":
          print ("Lista Finalizada")
          break
         elif x=="FIN":
          print ("Lista Finalizada")
          break
        print ("")
        print ("Su reclamo ha sido registrado correctamente")
        input ("Pulse ENTER para regresar al menú")
        os.system('cls')
    

    elif mot==4:
        print ("Por favor explique el inconveniente en un párrafo:")
        input ()
        print ("")
        print ("Su reclamo ha sido registrado correctamente")
        input ("Pulse ENTER para regresar al menú")
        os.system('cls')
   
    elif mot==5:
        print ("Sesión Finalizada")
    
    else:
        print ("ERROR, por favor presione ENTER")
        os.system('cls')
    
    if mot==5:
        break

