def menu():
    print("===GESTOR DE GASTOS===")
    print("1. Agregar gasto")
    print("2. Ver gasto")
    print("3. Buscar por categoria")
    print("4. Ver total gastado")
    print("5. Salir")
    opcion=int(input("Ingrese una opcion correcta: "))
    return opcion

lista_gasto=[]
def agregar_gasto(lista_gasto):
    descripcion=input("Ingrese la descripcion del gasto: ")
    categoria=input("Ingrese la categoria del gasto: ")
    monto=int(input("Ingrese el monto del gasto: "))
    lista_gasto.append({ 
        "descripcion": descripcion,
        "categoria": categoria,
        "monto":monto
        }
    )

def ver_gasto(lista_gasto):
    for l in lista_gasto: #Recorre cada gasto individualmente
        for clave, valor in l.items(): # De cada gasto agarramos la clave , valor
            print(f"{clave} | {valor}")


def buscar_por_categoria(lista_gasto):
    categoria_buscar=input("Ingrese la categoria que quiere buscar: ")
    for l in lista_gasto:
       if l["categoria"] == categoria_buscar:
           print(f"Gasto:{l["descripcion"]}| {l["categoria"]}, | {l["monto"]}")

def ver_total_gastado(lista_gasto):
    monto_total=0
    for l in lista_gasto:
        monto_total+=l["monto"]
    return monto_total




opc=0
while opc != 5:
    opc=menu()
    if opc == 1:
        agregar_gasto(lista_gasto)
        print("Se agrego el gasto correctamente")
    elif opc == 2:
        print("== GASTOS ==")
        ver_gasto(lista_gasto)
    elif opc == 3:
        buscar_por_categoria(lista_gasto)
    elif opc == 4:
        total_gastado=ver_total_gastado(lista_gasto)
        print(total_gastado)
    elif opc == 5:
        print("Salio del sistema ...")
    else :
        print("Ingrese una opcion correcta")


