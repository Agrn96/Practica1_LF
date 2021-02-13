def ordenado(list):
    n = len(list) - 1

    for i in range(n):
        for j in range(0,n-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return(list)
    
    