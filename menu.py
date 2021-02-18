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
    if(x == 1):
        nombre.clear()
        datos.clear()
        command.clear()
        cargar_Archivo.cargar_Archivo(nombre, datos, command)
    elif(x == 2):
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "O"):
                    print_Ordenada(nombre[i], datos[i])
                    break
    elif(x == 3):
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "B"):
                    print_Busqueda(command[i][j+1], datos[i], nombre[i])

    elif(x == 4):
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "O"):
                    print_Ordenada(nombre[i], datos[i])
                elif(command[i][j] == "B"):
                    print_Busqueda(command[i][j+1], datos[i], nombre[i])

    elif(x == 5):
        crear.crear_html(nombre, datos, command)
    else:
        print("Saliendo del applicacion")
        raise SystemExit(0)


def print_Ordenada(nombre, datos):
    temp_l = ordenado.ordenado(datos.copy())
    print(nombre, end=': ')
    print("ORDENADOS = ", end='')
    for i in temp_l:
        print(i, end=" ")
    print()


def print_Busqueda(command, datos, nombre):
    temp_l = busquedas.busquedas(datos, command)
    print(nombre, end=' = ')
    for k in datos:
        print(k, end=' ')

    print("BUSQUEDA POSICIONES = ", end='')
    for k in temp_l:
        print(k, end=' ')
    print()