import requests # Libreria que puede pedir peticiones HTTP a la api de peliculas

def menu():
    print("==CLIENTE DE PELICULAS==")
    print("1.Buscar pelicula")
    print("2.Ver detalle de una pelicula")
    print("3.Salir")
    opciones=int(input("Ingrese una opcion correcta: "))
    return opciones

def buscar_pelicula():
    url_movie="https://api.themoviedb.org/3/search/movie" #Hago un ENDPOINT que comunica el programa en python con la base de datos de peliculas
    buscar_pelicula=input("Ingrese la pelicula que quiera: ")

    mis_parametros= { #La APIKEY dice quien es el que esta mandando el mensaje.
        "api_key":"a38645be8fcae934620057f94fa16813", 
        "query": buscar_pelicula # Ingreso de dato
        } 

    solicitud=requests.get(url_movie,params=mis_parametros) #Consulto datos
    if solicitud.status_code == 200:
        datos_json= solicitud.json() #
        contador=0
        for peliculas in datos_json["results"]:
            contador += 1
            print(F"{contador}: ",peliculas["title"])
            print(peliculas["vote_average"])
            print(peliculas["release_date"])

            print("==========================")

        pelicula_buscada=int(input("Seleccione una: "))
        indice= pelicula_buscada - 1
        if pelicula_buscada >= 1 and pelicula_buscada <= len(datos_json["results"]):
            pelicula_seleccionada=datos_json["results"][indice]
            print(pelicula_seleccionada["title"])
            return pelicula_seleccionada["id"]
        else: 
            print("ERROR: Seleccionaste una opcion mayor a la que corresponde")
    else:
        print("Error a la peticion")
   
id_pelicula=buscar_pelicula()

    

def detalle_pelicula(id_pelicula):
    endpoint= f"https://api.themoviedb.org/3/movie/{id_pelicula}"
    acces_token= {
    "api_key" :"a38645be8fcae934620057f94fa16813"
    }
    solicitud=requests.get(endpoint,params=acces_token)
    if solicitud.status_code == 200:
        datos_json=solicitud.json()
        print(datos_json["overview"])


opc=0
while opc != 3:
    opc=menu()
    if opc == 1:
        buscar_pelicula()
    elif opc == 2:
        detalle_pelicula(id_pelicula)
    elif opc == 3:
        print("Saliste del programa")
    else:
        print("Elija una opcion correcta")