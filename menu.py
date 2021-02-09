from busquedas import busquedas
import cargar_Archivo
import ordenado
import busquedas
def menu():
    print("Menu Principal")
    print("1. Cargar Archivo de entrada")
    print("2. Desplegar listas ordenadas")
    print("3. Desplegar busquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. Salir")

    print("Choose Menu Option: ", end="\t")
    x = int(input())
    list = [1,4,2,3,5,6,2,3]
    if(x == 1):
        cargar_Archivo.cargar_Archivo()
    elif(x == 2):
        print("Placeholder")
        ordenado.ordenado(list.copy())
        print(list)
    elif(x == 3):
        print("Placeholder")
        busquedas.busquedas(list, 2)
    elif(x == 4):
        print("Placeholder")
        #Todas
    elif(x == 5):
        print("Placeholder")
        #Todas a archivo
    else:
        print("Saliendo del applicacion")
        raise SystemExit(0)