import tkinter
import busquedas
import cargar_Archivo
import ordenado
import crear


def crear_html(nombre, datos, command):

    name = "Practica1_LFP"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body>\n")
        for i in range(len(nombre)):
            for j in range(len(command[i])):
                if(command[i][j] == "O"):
                    temp_l = ordenado.ordenado(datos[i].copy())
                    f.write("<br>" + nombre[i] + ": ORDENADOS = ")
                    for k in temp_l:
                        f.write(k + " ")
                    f.write("</br>\n")
                elif(command[i][j] == "B"):
                    temp_l = busquedas.busquedas(datos[i], command[i][j+1])
                    f.write("<br>" + nombre[i] + ": ")
                    for k in datos[i]:
                        f.write(k + " ")
                    f.write("BUSQUEDA POSICIONES = ")
                    if(len(temp_l) == 0):
                        f.write("NO ENCONTRADO")
                    else:
                        for k in temp_l:
                            f.write(str(k) + " ")
                        f.write("</br>\n")
        f.write("\n</body>\n</html>")
