def busquedas(list, x):
    position = []
    for i in range(len(list)):
        if(list[i] == x):
            position.append(i+1)
    return(position)
    