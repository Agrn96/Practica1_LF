import class_listas
import menu
x = 0
while(x != 6):
    """Mientras x != 6, el menu sigue apareciendo
    """    
    print("")
    print("Menu Principal")
    print("1. Cargar Archivo de entrada")
    print("2. Desplegar listas ordenadas")
    print("3. Desplegar busquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. Salir")
    print("Choose Menu Option: ", end="\t")
    x = int(input())                #opcion del Menu
    lista = class_listas.Lista()    #Objeto del clase
    menu.menu(x, lista)             #Llamada al Menu utilizando el input del usuario
    