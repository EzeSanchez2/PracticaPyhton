from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class libros(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial:Optional[str]


diccionario_libro={}
contador=0
@app.post("/libros")
def insertar_libros(libro:libros):
    global contador #Usamos global para poder modificar la variable.
    contador += 1
    datos_libro={
        "titulo": libro.titulo,
        "autor": libro.autor,
        "paginas": libro.paginas,
        "editorial": libro.editorial
    }

    diccionario_libro[contador] = datos_libro

    return {"menssaje":f"Se inserto el libro ID {contador} , libro: {libro.titulo}"}

@app.get("/libros")
def obtener_tareas():
    return diccionario_libro
    
@app.get("/libros/{id}")
def mostrar_libro(id:int):
    if id in diccionario_libro:
        busqueda_id=diccionario_libro[id]
        return {"Libro": busqueda_id}

    return {"error":"El libro con ese ID no fue encontrado"}

@app.put("/libros/{id}")
def modificar_libro(id:int,libro:libros ):
    if id in diccionario_libro:
        datos_libros={
            "titulo": libro.titulo,
            "autor": libro.autor,
            "paginas": libro.paginas,
            "editorial": libro.editorial
        }
        diccionario_libro[id]= datos_libros
        return {"mensaje": f"Se modifico el libro ID: {id}" , "libro": datos_libros}
    else:
        return {"error": f"El libro con ID {id} no existe y no se puede modificar"}
        

    

@app.delete("/libros/{id}")
def eliminar_libro(id:int):
    if id in diccionario_libro:
        del diccionario_libro[id]
        return {"Libro_eliminado":f"El libro se a eliminado"}
    else:
        return {"Error": "No se encontro el ID"}




