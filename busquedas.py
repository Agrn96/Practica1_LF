def busquedas(list, x):
    position = []
    for i in range(len(list)-1):
        if(list[i] == x):
            position.append(i)
    print(x, position)
