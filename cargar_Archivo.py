from tkinter import *
from tkinter import filedialog

def cargar_Archivo(nombre, datos, command):
    filename = filedialog.askopenfile(filetypes=(('text files', 'txt'),))
    crear_listas(filename, nombre, datos, command)
    filename.close()

def crear_listas(filename, nombre, datos, command):
    n = 0
    for i in filename:
        datos.append([])
        command.append([])
        txt_c = i.split()
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

    