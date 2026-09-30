def menu():
    print("==AGENDA==")
    print("1.Agregar contacto")
    print("2.Ver contacto")
    print("3.Buscar contacto")
    print("4.Modificar contacto")
    print("5.Eliminar contacto")
    print("6.Salir")
    opciones=int(input("Ingrese una opcion: "))
    return opciones

lista_contacto={}

def agendar_contacto(lista_contacto):
    diccionario_interno={}
    nombre=input("Ingrese el nombre del contacto: ")
    lista_contacto[nombre]=diccionario_interno
    diccionario_interno["telefono"]=input("Ingrese el telefono del contacto: ")
    diccionario_interno["email"]=input("Ingrese el email del contacto: ")

def ver_contacto(lista_contacto):
    for clave,valor  in lista_contacto.items():
        print(f"{clave} | {valor}")

def buscar_contacto(lista_contacto):
    nombre_buscar=input("Ingrese el nombre del contacto: ")
    for clave,valor in lista_contacto.items():
        if clave == nombre_buscar:
            print(f"Contacto:{clave}|{valor}")

def modificar_contacto(lista_contacto):
    nombre_modificar=input("Ingrese el nombre a modificar: ")
    if nombre_modificar in lista_contacto:
        lista_contacto[nombre_modificar]["telefono"]=input("Ingrese el nuevo telefono: ")
        lista_contacto[nombre_modificar]["email"]=input("Ingrese el nuevo email: ")
    else:
        print("No existe ningun contacto con ese nombre")

def eliminar_contacto(lista_contacto):
    nombre_eliminar=input("Ingrese el nombre a eliminar: ")
    if nombre_eliminar in lista_contacto:
        del lista_contacto[nombre_eliminar]
    else:
        print("No existe ese nombre para eliminar")
            

opc=0
while opc != 6:
    opc=menu()
    if opc == 1:
        agendar_contacto(lista_contacto)
        print("Se agrego el contacto correctamente")
    elif opc == 2:
        print("Lista de contactos: ")
        ver_contacto(lista_contacto)
    elif opc == 3:
        buscar_contacto(lista_contacto)
    elif opc == 4:
        modificar_contacto(lista_contacto)
    elif opc == 5:
        eliminar_contacto(lista_contacto)
    elif opc == 6:
        print("Saliste del programa")
    else:
        print("Seleccione una opcion correcta")