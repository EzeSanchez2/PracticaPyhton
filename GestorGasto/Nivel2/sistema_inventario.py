def menu():
    print("==SISTEMA DE INVENTARIOS==")
    print("1.Agregar producto")
    print("2.Ver productos")
    print("3.Buscar producto")
    print("4.Modificar producto")
    print("5.Eliminar producto")
    print("6.Vender producto")
    print("7.Reponer stock")
    print("8.Mostrar productos con stock bajos")
    print("9.Mostrar total valor del inventario")
    print("10.Salir del sistema")
    opciones=int(input("Ingrese una opcion correcta: "))
    return opciones

lista_productos={}

def agregar_productos(lista_productos):
    diccionario_interno={}
    Id=int(input("Ingresar el id del producto: "))
    if Id in lista_productos:
        print("Ya existe un producto con ese ID")
    else:
        lista_productos[Id]= diccionario_interno
        diccionario_interno["nombre"]=input("Ingrese el nombre del producto: ")
        diccionario_interno["precio"]=int(input("Ingrese el precio del producto: "))
        diccionario_interno["stock"]=int(input("Ingrese el stock del pruducto: "))
        diccionario_interno["categoria"]=input("ingrese la categoria del producto: ")

def ver_productos(lista_productos):
    for clave , valor in lista_productos.items():
        print(f"{clave}|{valor}")

def buscar_producto(lista_productos):
    id_buscar=int(input("Ingrese el ID del producto: "))
    for clave, valor in lista_productos.items():
        if clave == id_buscar:
            print(f"{clave}|{valor}")

def modificar_producto(lista_productos):
    id_modificar=int(input("Ingrese el ID a modificar: "))
    if id_modificar in lista_productos:
        lista_productos[id_modificar]["nombre"]=input("Ingrese el nombre modificado: ")
        lista_productos[id_modificar]["precio"]=input("Ingrese el precio modificado: ")      
        lista_productos[id_modificar]["stock"]=input("Ingrese el stock modificado: ")
        lista_productos[id_modificar]["categoria"]=input("Ingrese la categoria modificado: ")
    else:
        print("No existe ningun producto con ese ID")

def eliminar_producto(lista_productos):
    id_eliminar=int(input("Ingrese el ID a eliminar: "))
    if id_eliminar in lista_productos:
        del lista_productos[id_eliminar]
    else:
        print("No se encontro el ID para eliminar")

def vender_producto(lista_productos):
    id_vender=int(input("Ingrese el ID del producto que quiere vender: "))
    if id_vender in lista_productos:
        cantidad_vender=int(input("Cuantas cantidades queres vender: "))
        if lista_productos[id_vender]["stock"] >= cantidad_vender:
            stockVendido=lista_productos[id_vender]["stock"] - cantidad_vender
            print(f"Listo se a vendido {stockVendido}")

        else:
            print("No hay esa cantidad de stock el disponible")
    else:
        print("No se encuentra el ID que quiere vender")
    
opc=0
while opc != 10:
    opc=menu()
    if opc == 1:
        agregar_productos(lista_productos)
    elif opc == 2:
        ver_productos(lista_productos)
    elif opc == 3:
        buscar_producto(lista_productos)
    elif opc == 4:
        modificar_producto(lista_productos)
    elif opc == 5:
        eliminar_producto(lista_productos)
    elif opc == 6:
        print("Se esta vendiendo el producto")
    elif opc == 7:
        print("Se esta reponiendo el stock")
    elif opc == 8:
        print("Se esta mostrando  productos con stock bajo")
    elif opc == 9:
        print("Se esta mostando el valor del inventario")
    elif opc == 10:
        print("Saliste del sistema")
    else:
        print("Elija una opcion correcta")