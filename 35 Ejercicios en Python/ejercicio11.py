#Ejercicios del 11-15: Estructuras secuenciales y estructuras selectivas

# Ejercicio 11: Sistema de datos de RENIEC

print ("Sistema de datos de RENIEC")

DNI=int(input("Por favor, ingrese el DNI: "))

if DNI == 72531804:
    print ("NOMBRES Y APELLIDOS: GERARDO ANTONIO URDIALES VEGA")
    print ("FECHA DE NACIMIENTO: 23/05/1989")
    print ("UBIGEO DE NACIMIENTO: 200569")
    print ("DEPARTAMENTO: LIMA")
    print ("PROVINCIA: LIMA")
    print ("DISTRITO: SANTIAGO DE SURCO")
    print ("LUGAR DE RESIDENCIA: JR.BOLOGNESI 275-CERCADO")
    print ("SEXO: MASCULINO")
    print ("ESTADO CIVIL: SOLTERO")
elif DNI==82531804:
    print ("NOMBRES Y APELLIDOS: JHON JESUS OSORIO NASMIENTO")
    print ("FECHA DE NACIMIENTO: 12/06/1993")
    print ("UBIGEO DE NACIMIENTO: 190110")
    print ("DEPARTAMENTO: LIMA")
    print ("PROVINCIA: LIMA")
    print ("DISTRITO: LA MOLINA")
    print ("LUGAR DE RESIDENCIA: AV. LAS FRESIAS 128")
    print ("SEXO: MASCULINO")
    print ("ESTADO CIVIL: CASADO")
elif DNI==72531604:
    print ("NOMBRES Y APELLIDOS: MARIA JOSE SILVA CASTILLO")
    print ("FECHA DE NACIMIENTO: 23/04/2002")
    print ("UBIGEO DE NACIMIENTO: 190360")
    print ("DEPARTAMENTO: LIMA")
    print ("PROVINCIA: LIMA")
    print ("DISTRITO: CHORRILLOS")
    print ("LUGAR DE RESIDENCIA: AV. DEFENSORES DEL MORRO Nº2765")
    print ("SEXO: FENEMINO")
    print ("ESTADO CIVIL: CASADA")
    
else:
    print ("Por favor, verifique que los números hayan sido escritos correctamente")   


print ("Fin del sistema")