from tkinter import *
from tkinter import filedialog

import busquedas
import cargar_Archivo
import ordenado
import busquedas
def menu():
    nombre = []
    datos = []
    command = []

    print("Menu Principal")
    print("1. Cargar Archivo de entrada")
    print("2. Desplegar listas ordenadas")
    print("3. Desplegar busquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. Salir")

    print("Choose Menu Option: ", end="\t")
    x = int(input())
    list = [1,4,2,3,5,6,2,3]
    if(x == 1):
        filename = cargar_Archivo.cargar_Archivo()
        crear_listas(filename, nombre, datos, command)
        print(filename)
        print(nombre)
        print(datos)
        print(command)
    elif(x == 2):
        print("Placeholder")
        ordenado.ordenado(list.copy())
        print(list)
    elif(x == 3):
        busquedas.busquedas(list, 2)
    elif(x == 4):
        ordenado.ordenado(list.copy())
        busquedas.busquedas(list, 2)
        busquedas.busquedas(list, 3)
    elif(x == 5):
        ordenado.ordenado(list.copy())
        busquedas.busquedas(list, 2)
        busquedas.busquedas(list, 3)
    else:
        print("Saliendo del applicacion")
        raise SystemExit(0)

def crear_listas(filename, nombre, datos, command):
    n=0
    for i in filename:
        datos.append([])
        command.append([])
        txt_c = i.split()
        txt = i.replace(" ","")
        print(txt_c)
        for j in range(len(txt_c)):
            if(j==0):
                nombre.append(txt_c[0])
            elif(txt_c[j] == "BUSCAR"):
                command[n].append("B")
                command[n].append(txt_c[j+1])
                break
            elif(txt_c[j] == "ORDENAR" or txt_c[j] == "ORDENAR,"):
                command[n].append("O")
            else:
                temp_s = txt_c[j]
                temp_c = ""
                for k in range(len(temp_s)):
                    if(temp_s[k].isdigit() and k+1 == len(temp_s)):
                        datos[n].append(temp_s[k])
                        temp_c = ""
                    elif(temp_s[k].isdigit()):
                        temp_c += temp_s[k]
                    elif(temp_c != ""):
                        datos[n].append(temp_c)
                        temp_c = ""
                    print(k)
        n+=1

