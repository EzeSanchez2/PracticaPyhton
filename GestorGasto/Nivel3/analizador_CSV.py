import csv

def menu():
    print("==ANALIZADOR CSV==")
    print("1.Mostrar ventas")
    print("2.Buscar ventas por productos")
    print("3.Calcular total vendido")
    print("4.Mostrar productos mas vendidos")
    print("5.Mostrar venta de mayor importe")
    print("6.Mostrar ventas por fecha")
    print("7.Salir del programa")
    opciones=int(input("Ingrese una opcion: "))
    return opciones

archivo=open("GestorGasto/Nivel3/ventas.csv","r") #Abro el archivo
lector=csv.reader(archivo) # Lee el archivo 
next(lector) #Saltea el encabezado



lista_ventas=[]
for fila in lector:
    ventas={}
    ventas["ID"]=int(fila[0])
    ventas["Producto"]=fila[1]
    ventas["Categoria"]=fila[2]
    ventas["Precio"]=int(fila[3])
    ventas["Cantidad"]=int(fila[4])
    ventas["Fecha"]=fila[5]  
    lista_ventas.append(ventas)


def mostrar_ventas(lista_ventas):
    for ventas in lista_ventas:
        print(ventas)

def buscar_ventas_productos(lista_ventas):
    producto_buscar=input("Ingrese el producto que quiera buscar: ")
    for ventas in lista_ventas:
        if ventas["Producto"] == producto_buscar:
            print(ventas["Producto"])

def total_vendido(lista_ventas):
    acumulador_venta=0
    for venta in lista_ventas:
        vendido=venta["Precio"] * venta["Cantidad"]
        acumulador_venta += vendido
    print(f"La cantidad total vendido fue de:{acumulador_venta}")

def productos_mas_vendidos(lista_ventas):
    p_mas_vendidos=0
    nombre_p_vendido=""
    ventas_por_productos={}
    for ventas in lista_ventas:
        if ventas["Producto"] in ventas_por_productos:
            ventas_por_productos[ventas["Producto"]] += ventas["Cantidad"]
        else:
            ventas_por_productos[ventas["Producto"]] = ventas["Cantidad"]
    for clave, valor in ventas_por_productos.items():
        if valor > p_mas_vendidos:
            p_mas_vendidos=valor
            nombre_p_vendido=clave
                
            



        



        




opc=0
while opc != 7:
    opc=menu()
    if opc == 1:
        mostrar_ventas(lista_ventas)
    elif opc == 2:
        buscar_ventas_productos(lista_ventas)
    elif opc == 3:
        total_vendido(lista_ventas)
    elif opc == 4:
        print("Se esta mostrando los productos mas vendidos")
    elif opc == 5:
        print("Se esta mostrando venta de mayor importe")
    elif opc == 6:
        print("Se esta mostrando ventas por fecha")
    elif opc == 7:
        print("Saliste del programa")
    else:
        print("Seleccione una opcion correcta")


