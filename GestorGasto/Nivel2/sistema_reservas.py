from datetime import datetime

def menu():
    print("==SISTEMA DE RESERVAS==")
    print("1.Crear reserva")
    print("2.Ver reserva")
    print("3.Buscar reserva")
    print("4.Modificar reserva")
    print("5.Cancelar reserva")
    print("6.Ver reservas de una fecha")
    print("7.Salir del sistema")
    opciones=int(input("Ingrese una opcion: "))
    return opciones

lista_reservas={}
def crear_reservas(lista_reservas):
    diccionario_interno={}
    Id=int(input("Ingrese el ID de la reserva: "))
    if Id in lista_reservas:
        print("El ID ya existe en la lista")
    else:
        lista_reservas[Id]= diccionario_interno
        diccionario_interno["nombres"]=input("Ingrese el nombre del huesped: ")

        #INGRESO DE FECHA
        while True:
            diccionario_interno["fecha"]=input("Ingrese la fecha de la reserva: ")
            try:
                fecha=datetime.strptime(diccionario_interno["fecha"], "%d/%m/%Y")
                diccionario_interno["fecha"]= fecha
                break
            
            except ValueError:
                print("Pusiste una fecha con un formato invalido: El formato tiene que ser: %d/%m/%Y ")
                

        #INGRESO DE HORA
        while True:
            diccionario_interno["hora"]=input("Ingrese la hora de la reserva: ")
            try:
                hora=datetime.strptime( diccionario_interno["hora"], "%H:%M")
                diccionario_interno["hora"]=hora
                break

            except ValueError:
                print("Pusiste una hora con un formato invalido. El formato tiene que ser: %H:%M ")
                
       
        
        while True:
            diccionario_interno["cantidad_personas"]=int(input("Ingrese la cantidad de personas: "))
            if diccionario_interno["cantidad_personas"] > 0:
                break
            else:
                print("Seleccione un numero correcto")

        diccionario_interno["estado"]= "confirmada"

def ver_reserva(lista_reservas):
    for clave,valor in lista_reservas.items():
        print(f"{clave}| {valor}")

def buscar_reserva(lista_reservas):
    id_buscar=int(input("Ingrese el ID que quiere buscar: "))
    for clave , valor in lista_reservas.items():
        if clave == id_buscar:
            print(f"{clave}| {valor}")

def modificar_reserva(lista_reservas):
    id_modificar=int(input("Ingrese el ID que quiere modificar: "))
    if id_modificar in lista_reservas:
        lista_reservas[id_modificar]["nombres"]=input("Ingrese el nuevo nombre del huesped: ")
        #FECHA
        while True:
            lista_reservas[id_modificar]["fecha"]=input("Ingrese la nueva fecha del huesped: ")
            try:
                fecha=datetime.strptime(lista_reservas[id_modificar]["fecha"], "%d/%m/%Y")
                lista_reservas[id_modificar]["fecha"]=fecha
                break
            except ValueError:
                print("Pusiste una fecha con un formato invalido: El formato tiene que ser: %d/%m/%Y ")
                
        #HORA
        while True:
            lista_reservas[id_modificar]["hora"]=input("Ingrese la nueva hora del huesped: ")
            try:
                hora=datetime.strptime(lista_reservas[id_modificar]["hora"], "%H:%M" )
                lista_reservas[id_modificar]["hora"]=hora
                break
            except ValueError:
                print("Pusiste una hora con un formato invalido: El formato tiene que ser : %H:%M")

        while True:
            lista_reservas[id_modificar]["cantidad_personas"]= int(input("Ingrese la nueva cantidad de personas: "))
            if lista_reservas[id_modificar]["cantidad_personas"] > 0:
                break
            else:
                print("Seleccione un numero correcto")
        

        lista_reservas[id_modificar]["estado"]= "confirmada"

def cancelar_reserva(lista_reservas):
    id_cancelar=int(input("Ingrese el ID que quiere eliminar: "))
    if id_cancelar in lista_reservas:
        lista_reservas[id_cancelar]["estado"]= "cancelada"
    else:
        print("No se encontro el ID ingresado")

def ver_reserva_fecha(lista_reservas):
    fecha_buscar=input("Ingrese la fecha de la reserva que quiere ver: ")
    t_fecha=datetime.strptime(fecha_buscar,"%d/%m/%Y")
    encontrada=False
    for clave, valor in lista_reservas.items():
        if lista_reservas[clave]["fecha"] == t_fecha:
            print(f"{clave}| {valor}")
            encontrada=True
    if encontrada == False:
        print("No se encontro la fecha de la reserva")
        
opc=0
while opc != 7:
    opc=menu()
    if opc == 1:
        crear_reservas(lista_reservas)
        print("Se creo la reserva")
    elif opc == 2:
        ver_reserva(lista_reservas)
    elif opc == 3:
        buscar_reserva(lista_reservas)
    elif opc == 4:
        modificar_reserva(lista_reservas)
    elif opc == 5:
        cancelar_reserva(lista_reservas)
    elif opc == 6:
        ver_reserva_fecha(lista_reservas)
    elif opc == 7:
        print("Saliste del sistema")
    else:
        print("Seleccione una opcion correcta")