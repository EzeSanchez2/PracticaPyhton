def menu():
    print("===GESTOR DE GASTOS===")
    print("1. Agregar gasto")
    print("2. Ver gasto")
    print("3. Buscar por categoria")
    print("4. Ver total gastado")
    print("5. Salir")
    opcion=int(input("Ingrese una opcion correcta: "))
    return opcion

opc=0
while opc != 5:
    opc=menu()
    if opc == 1:
        print("Se agregando el gasto")
    elif opc == 2:
        print("Se vio el gasto")
    elif opc == 3:
        print("Se busca por categoria")
    elif opc == 4:
        print("Se esta viendo el total gastado")
    elif opc == 5:
        print("Salio del sistema ...")
    else :
        print("Ingrese una opcion correcta")


