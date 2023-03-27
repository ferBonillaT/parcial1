#Main program
'''
codigo del programa principal de ejecucion de toda la logica y de funciones.
'''
from crud import*


from basiFunciones import*

while True:
    print("Menu")
    print("1.buscar libros por fecha")
    print("2.Buscar un libro por su titulo")
    print("3.Agregar un libro")
    print("4.Actualizar")
    print("5.eliminar")
    print("6.salir")

    opcion =input("Opcion: ")
    if opcion =="1":
        fecha = int(input("fecha del libro: "))
        consultar_libros_por_año(fecha)
    elif opcion =="2":
        titulo = input("cual es el titulo del libro: ").lower()
        consultar_libro_por_titulo(titulo)
        print("algo")
    elif opcion == "3":
        libro = agregar_libro()
        create_libro(libro)
        print("algo")
    elif opcion =="4":
        id = int(input("ingrese id del Libro: "))
        libro = update_libro()
        updateLibro(id,libro)


        print("algo")
    elif opcion == "5":
        id = int(input("ingrese el id del libro: "))
        if id is not None:
            confirmacion = input("seguro que desea eliminar el registro(si/no): ").lower()
            if confirmacion == "si":
                delete_libro(id)
            elif confirmacion == "no":
                print("cancelado.....")
        else:
            print("opcion no valida..")
        print("algo")
    elif opcion == "6":
        break
    else:
        print("opcion no validad...")
