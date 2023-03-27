#funciones basicas
from conectionMongodb import db

#funcion agregar
def agregar_libro():
    id =int(input("id: "))
    titulo = input("nombre del libro: ")
    autor = input("autor: ")
    pais = input("Pais: ")
    fecha_publicacion = int(input("Fecha de publicacion: "))

    libro ={
        "_id": id,
        "titulo": titulo,
        "autor":autor,
        "pais":pais,
        "fecha_publicacion":fecha_publicacion
    }
    return libro

#funcion consultar un libro por su titulo
def consultar_libro_por_titulo(titulo):
    # buscar el libro por su título
    libro = db.libros.find_one({"titulo": titulo})

    # imprimir el resultado
    if libro:
        print(libro)
    else:
        print("El libro no fue encontrado.")

'''funcion actualizar '''
def update_libro():
    id =int(input("id: "))
    titulo = input("nombre del libro: ")
    autor = input("autor: ")
    pais = input("Pais: ")
    fecha_publicacion = int(input("Fecha de publicacion: "))

    libro ={
        "_id": id,
        "titulo": titulo,
        "autor":autor,
        "pais":pais,
        "fecha_publicacion":fecha_publicacion
    }
    return libro

#esta funcion permite actualizar
# todo el documento o solo una parte
#ejemplo titulo sera igual a lo que le pase el usuario para modificar el titulo del libro
def update_libro():
    print("menu de opciones")
    print("1. Modificar los datos del libro")
    print("2. Modificar solo un elemento de la descripcion del libro")
    opcion = input("Opcion: ")

    if opcion =="1":
        titulo = input("nombre del libro: ")
        autor = input("Nombre del autor: ")
        pais = input("Pais: ")
        fecha_publicacion = int(input("Fecha: "))

        libro = {
            "titulo": titulo,
            "autor": autor,
            "pais": pais,
            "fecha_publicacion": fecha_publicacion
        }
        return libro
    elif opcion =="2":
        indice =input("Ingrese el valor del indice: ")
        valor =input("ingrese valor a modificar: ")
        libro = {indice:valor}
    return libro