#!/usr/bin/python
#-*- coding: utf-8 -*-

def lee_cadena(nombre):
    archivo = open("cadena.dat", "r")
    contenido = archivo.readline().rstrip("\n")
    contenido = list(contenido)
    archivo.close()
    return contenido

def invierte(datos):
    cadena = ""
    for letra in datos:
        if letra == "A":
            cadena = cadena + "T"
        elif letra == "T":
            cadena = cadena + "A"
        elif letra == "C":
            cadena = cadena + "G"
        elif letra == "G":
            cadena = cadena + "C"
        else:
            print("\nCARACTER NO ENCONTRADO\n")
     
    archivo = open("helice.dat", "w")
    archivo.write(cadena)
    archivo.close()
    return(cadena)


def lee_cadena2(nombre):
    archivo = open("helice.dat", "r")
    contenido = archivo.readline()
    contenido = list(contenido)
    archivo.close()
    return contenido


print("1.- Ejecutar y no mostrar")
print("2.- Ejecutar y mostrar")
opcion = input("Escoger opcion: ")

if (int(opcion)==1):
    cadena_inv = lee_cadena2('nombre')
    print(cadena_inv)
    print("Ejecutado correctamente")
    
elif(int(opcion)==2):
    cadena = lee_cadena('cadena.dat')
    cadena_inv = lee_cadena2('nombre')
    print(cadena, cadena_inv)
else:
    print("Su valor no coincide")
    

    
if __name__ == "__main__":
    datos = lee_cadena("cadena.dat")
    datos2 = lee_cadena("helice.dat")
    cad_invertida = invierte(datos)
    
    
    
    