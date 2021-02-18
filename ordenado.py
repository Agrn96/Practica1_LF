def ordenado(lista):
    n = len(lista) - 1

    for i in range(n):
        for j in range(0,n-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return(lista)
    
    