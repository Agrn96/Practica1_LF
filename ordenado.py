def ordenado(lista):
    """Funcion para ordenar la lista utilizando sorteo de burbuja

    Args:
        lista (int[]): Una lista de numeros desordenadas
    """    
    n = len(lista) - 1

    for i in range(n):
        for j in range(0,n-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return(lista)
    
    