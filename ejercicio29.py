
# Ejercicio 29: PCálculo de Promedio Escolar
import os
ind="si"
des=0
apro=0

print ("Sistema de Cálculo de Promedio Escolar")
while ind!="no" and ind=="si":
    print ("-"*100)
    print ("NOTA: \n La Nota Nº1: Trabajos académicos \n La Nota Nº2: Examen Bimestral \n La Nota Nº3: Exposiciones")
    print ("-"*100)
    print ("Ingresar el nombre del Curso:")
    name=input()
    eva=3
    suma=0
    for i in range (1, eva+1):
        num=float(input("Ingrese la nota Nº{}:  ".format(i))) 
        suma+=num
        promedio=suma/eva
    if promedio>=10.5:
        print ("Tu promedio final en el curso de {} es {:.3f}".format(name,promedio))
        print ("Te encuentras aprobado")
        apro=apro+1
        ind=input ("¿Deseas sacar promedio de otro curso?")
        os.system('cls')
    else:
        print ("Tu promedio final en el curso de {} es {:.3f}".format(name,promedio))
        print ("Te encuentras desaprobado")
        des=des+1
        ind=input ("¿Deseas sacar promedio de otro curso?")
        if ind=="si":
            os.system('cls')
        else:
            print ("")

print ("*"*100)           
print ("El total de cursos aprobados es: ",apro)
print ("El total de cursos desaprobados es: ",des)   
print ("Fin del sistema")



