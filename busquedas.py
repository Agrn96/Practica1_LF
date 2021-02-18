def busquedas(lista, x):
    position = []
    for i in range(len(lista)):
        if(lista[i] == x):
            position.append(i+1)
    return(position)
    