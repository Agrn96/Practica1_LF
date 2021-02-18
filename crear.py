import busquedas
import ordenado

def crear_html(lista):
    """Funcion para crear el html utilizando el informacion de las listas

    Args:
        lista (class): Listas con informacion
    """
    name = "Practica1_LFP"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body>\n")
        for i in range(len(lista.nombre)):
            for j in range(len(lista.command[i])):
                if(lista.command[i][j] == "O"):
                    temp_l = ordenado.ordenado(lista.datos[i].copy())
                    f.write("<br>" + lista.nombre[i] + ": ORDENADOS = ")
                    for k in temp_l:
                        f.write(k + " ")
                    f.write("</br>\n")
                elif(lista.command[i][j] == "B"):
                    temp_l = busquedas.busquedas(lista.datos[i], lista.command[i][j+1])
                    f.write("<br>" + lista.nombre[i] + ": ")
                    for k in lista.datos[i]:
                        f.write(k + " ")
                    f.write("BUSQUEDA POSICIONES = ")
                    if(len(temp_l) == 0):
                        f.write("NO ENCONTRADO")
                    else:
                        for k in temp_l:
                            f.write(str(k) + " ")
                        f.write("</br>\n")
        f.write("\n</body>\n</html>")
