from tkinter import *
from tkinter import filedialog

import busquedas
import cargar_Archivo
import ordenado
import crear

nombre = []
datos = []
command = []


def menu(x):
    list = [1, 4, 2, 3, 5, 6, 2, 3]
    if(x == 1):
        nombre.clear()
        datos.clear()
        command.clear()
        filename = cargar_Archivo.cargar_Archivo()
        crear_listas(filename, nombre, datos, command)
        filename.close()
    elif(x == 2):
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "O"):
                    temp_l = ordenado.ordenado(datos[i].copy())
                    print(nombre[i], end=': ')
                    print("ORDENADOS = ", end='')
                    for i in temp_l:
                        print(i, end=" ")
                    print()
                    break
    elif(x == 3):
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "B"):
                    temp_l = busquedas.busquedas(datos[i], command[i][j+1])
                    print(nombre[i], end=' = ')
                    for k in datos[i]:
                        print(k, end=' ')

                    print("BUSQUEDA POSICIONES = ", end='')
                    for i in temp_l:
                        print(i, end=' ')
                    print()
                    break

    elif(x == 4):
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "O"):
                    temp_l = ordenado.ordenado(datos[i].copy())
                    print(nombre[i], end=': ')
                    print("ORDENADOS = ", end='')
                    for k in temp_l:
                        print(k, end=" ")
                    print()
                elif(command[i][j] == "B"):
                    temp_l = busquedas.busquedas(datos[i], command[i][j+1])
                    print(nombre[i], end=' = ')
                    for k in datos[i]:
                        print(k, end=' ')

                    print("BUSQUEDA POSICIONES = ", end='')
                    for k in temp_l:
                        print(k, end=' ')
                    print()

    elif(x == 5):
        crear.crear_html(nombre, datos, command)
    else:
        print("Saliendo del applicacion")
        raise SystemExit(0)


def crear_listas(filename, nombre, datos, command):
    n = 0
    for i in filename:
        datos.append([])
        command.append([])
        txt_c = i.split()
        txt = i.replace(" ", "")
        for j in range(len(txt_c)):
            if(j == 0):
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
        n += 1
