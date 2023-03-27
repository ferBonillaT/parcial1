#conexion a mondodb datos de la data base
import pymongo
cliente =pymongo.MongoClient("mongodb://localhost:27017/");
db = cliente['biblioteca1']

collections =db['libros']