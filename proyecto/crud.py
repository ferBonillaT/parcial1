#crud para el programa

from conectionMongodb import*


#aqui esta una funcion la cual resive el año de los libros a consutar osea los filtra por fecha
#y aparecen los libros relacionados con la fecha ejemplo consultal libros de 1959
def consultar_libros_por_año(fecha):
    # buscar todos los libros con el año de publicación especificado
    libros = db.libros.find({"fecha_publicacion": fecha})

    # imprimir los resultados
    for libro in libros:
        print(libro)

#esta funcion crea un libro y lo agrega
def create_libro(libro):
    result =collections.insert_one(libro)
    print(result.inserted_id)
#funcion de actualizar
def updateLibro(id,json_indices_values):
    query ={"_id":id}
    new_values ={"$set": json_indices_values}
    result =collections.update_one(query,new_values)
    print(result.modified_count)
#funcion de eliminar
def delete_libro(id=None):
    if id is not None:
        query = {"_id": id}
        result = collections.delete_one(query)
        print("se elimino...")
    else:
        print("no se encontro registro")