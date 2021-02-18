from tkinter import *
from tkinter import filedialog


def cargar_Archivo(lista):
    """Funcion para abrir el archivo que se utiliza para la programa

    Args:
        lista (class): Listas para guardar informacion del archivo
    """
    filename = filedialog.askopenfile(filetypes=(('text files', 'txt'),))
    crear_listas(filename, lista)
    filename.close()


def crear_listas(filename, lista):
    """Funcion para crear las listas utilizando el informacion del archivo

    Args:
        filename (String): Nombre del archivo
        lista (class): Listas para guardar informacion del archivo
    """
    n = 0  # numero para el for loop
    for i in filename:  # for loop que utiliza los datos del archivo
        lista.datos.append([])  # Agregando un nested list
        lista.command.append([])  # Agregando un nested list
        txt_c = i.split()  # Split los strings en el archivo por espacios
        for j in range(len(txt_c)):  # For loop para navegar el string
            if(j == 0):
                lista.nombre.append(txt_c[0])  # Agrega el nombre de la lista
            elif(txt_c[j] == "BUSCAR"):
                lista.command[n].append("B")
                lista.command[n].append(txt_c[j+1])
                break
                # Agrega la busqueda de la lista, asumiendo que el busque siempre esta en el fin del String
            elif(txt_c[j] == "ORDENAR" or txt_c[j] == "ORDENAR,"):
                lista.command[n].append("O")  # Agrega que la lista se ordena
            else:  # Agrega los datos de la lista tomando en caso espacios, commas y numeros con multiple digitos
                temp_s = txt_c[j]
                temp_c = ""
                for k in range(len(temp_s)):
                    if(temp_s[k].isdigit() and k+1 == len(temp_s)):
                        lista.datos[n].append(temp_s[k])
                        temp_c = ""
                    elif(temp_s[k].isdigit()):
                        temp_c += temp_s[k]
                    elif(temp_c != ""):
                        lista.datos[n].append(temp_c)
                        temp_c = ""
        n += 1
