def busquedas(lista, x):
    """Funcion para buscar el numero en una lista de datos

    Args:
        lista (int []): Lista de datos 
        x (int): numero que se encuentra en la lista de datos
    """
    position = []
    for i in range(len(lista)):
        if(lista[i] == x):
            position.append(i+1)
    return(position)
