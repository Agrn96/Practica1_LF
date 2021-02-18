from tkinter import *
from tkinter import filedialog

import busquedas
import cargar_Archivo
import ordenado
import crear

def menu(x, lista):
    """Función que se llama según la entrada del usuario para el menú

    Args:
        x (int)  
            1 : Cargar Archivo  -   Se Carga un archivo de .txt y agrega el informacion 
                                    a las listas del programa
            2 : Desplegar ordenadas -   Se desplega las listas ordenadas que piden que sean
                                        ordenadas
            3 : Desplegar busquedas -   Se desplega los posiciones del numero que encuentra
                                        en las listas
            4 : Desplegar todo      -   Se desplega ambas listas ordenadas y posiciones del 
                                        numero que se encuentra en las listas
            5 : Desplegar todas a archivo   -   Se desplega ambas listas ordenadas y posiciones del 
                                                numero que se encuentra en las listas en un html utilizando tkinter
            6 : Salir   -   Se cierra el aplicacion
    Raises:
        SystemExit: Menu(6)
    """
    if(x == 1):  # Menu Opcion 1: Cargar Archivo
        # Borrar los datos de las listas si se carga archivos seguidos
        lista.nombre.clear()
        lista.datos.clear()
        lista.command.clear()
        # Llamada al funcion para cargar el archivo
        cargar_Archivo.cargar_Archivo(lista)
    elif(x == 2):
        # For Loop para navegar las listas
        for i in range(len(lista.nombre)):
            for j in range(len(lista.command[i])):
                # Encuentra si la lista tiene la commanda de Ordenar (O)
                if(lista.command[i][j] == "O"):
                    # Imprimir los datos ordenadas
                    print_Ordenada(lista.nombre[i], lista.datos[i])
                    break
    elif(x == 3):
        # For Loop para navegar las listas
        for i in range(len(lista.nombre)):
            for j in range(len(lista.command[i])):
                # Encuentra si la lista tiene la commanda de Busqueda (B)
                if(lista.command[i][j] == "B"):
                    # Imprimir los posiciones del numero que se encuentra
                    print_Busqueda(
                        lista.command[i][j+1], lista.datos[i], lista.nombre[i])

    elif(x == 4):
        # For Loop para navegar las listas
        for i in range(len(lista.nombre)):
            for j in range(len(lista.command[i])):
                # Encuentra si la lista tiene la commanda de Ordenar (O)
                if(lista.command[i][j] == "O"):
                    # Imprimir los datos ordenadas
                    print_Ordenada(lista.nombre[i], lista.datos[i])
                # Encuentra si la lista tiene la commanda de Busqueda (B)
                elif(lista.command[i][j] == "B"):
                    # Imprimir los posiciones del numero que se encuentra
                    print_Busqueda(
                        lista.command[i][j+1], lista.datos[i], lista.nombre[i])

    elif(x == 5):
        # Llamada al funcion para agregar las listas en un html
        crear.crear_html(lista)
    else:
        print("Saliendo del applicacion")
        raise SystemExit(0)  # Se cierra la aplicacion


def print_Ordenada(nombre, datos):
    """Funcion para ordenar la lista y imprimir resultados

    Args:
        nombre (String): Nombre de la lista
        datos (Int[]): Datos de la lista
    """
    temp_l = ordenado.ordenado(datos.copy())
    print(nombre, end=': ')
    print("ORDENADOS = ", end='')
    for i in temp_l:
        print(i, end=" ")
    print()


def print_Busqueda(command, datos, nombre):
    """Funcion para encontrar el posicion del numero y imprimir los resultados
    Args:
        command (int): Numero que se encuentra
        datos (int[]): datos de la lista desordenada
        nombre ([type]): nombre de la lista
    """
    temp_l = busquedas.busquedas(datos, command)
    print(nombre, end=' = ')
    for k in datos:
        print(k, end=' ')

    print("BUSQUEDA POSICIONES = ", end='')
    for k in temp_l:
        print(k, end=' ')
    print()
