clientes = {
    "19571133-K": {
        "nombre" : "Ignacio Alonso Romero Gutierrez",
        "telefono" : "967673326",
        "mail" : "ign.romerog@duocuc.cl",
        "vigencia" : "S"
    } ,   
    "15432109-8": {
        "nombre" : "Juan Carlos Perez Soto",
        "telefono" : "955554433",
        "mail" : "ju.perezs@duocuc.cl",
        "vigencia" : "N"
    },
    "21948302-3": {
        "nombre" : "Diego Alejandro Valenzuela Fuenzalida",
        "telefono" : "933847291",
        "mail" : "di.valenzuelaf@yahoo.com",
        "vigencia" : "S"
    },
}
reservas = {}
sala_cine = [
             [ "1","2","3","4",     "5","6","7","8",    "9","10","11","12",],
             ["13","14","15","16", "17","18","19","20", "21","22","23","24",],
             ["25","26","27","28", "29","30","31","32", "33","34","35","36",],
             ["37","38","39","40", "41","42","43","44", "45","46","47","48",],
             ["49","50","51","52", "53","54","55","56", "57","58","59","60",],
             ["61","62","63","64", "65","66","67","68", "69","70","71","72",]
             ]

def obtener_asientos_reservados():
    asientos_ocupados = []
    for lista_asientos in reservas.values():
        for asiento in lista_asientos:
            asientos_ocupados.append(asiento)
    return asientos_ocupados

def crear_cliente():
    print("Ingresa tu Rut: ")
    Rut = input("Rut: ").strip().upper()
    if Rut in clientes:
        print("Usuario Ya Registrado")
        return
    else:
        print("Usuario No Registrado")
        print("Ingresa tu Nombre")
        nombre = input("Nombre: ")
        print("Ingresa tu telefono")
        telefono = input("Telefono: ")
        print("Ingresa tu correo")
        correo = input("Correo: ")
        
        while True:
            vigencia = input("Tiene vigencia? S / N: ").strip().upper()
            if vigencia == "S" or vigencia == "N":
                break
            else:
                print("Error: Ingrese solamente 'S' para Sí o 'N' para No.")  
        clientes[Rut] = {
            "nombre" : nombre,
            "telefono" : telefono,
            "mail" : correo,
            "vigencia" : vigencia
        }
        print("Cliente Registrado con exito")

def listar_cliente():
    if not clientes:
        print("No hay clientes registrados")
    else:
        print ("Lista de Clientes")
        for Rut, datos in clientes.items():
            print("===============================")
            print(f"RUT: {Rut}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Telefono: {datos['telefono']}")
            print(f"Mail: {datos['mail']}")
            print(f"Vigencia: {datos['vigencia']}")
            print("===============================")

def modificar_cliente():
    if not clientes:
        print("No se figuran clientes en el sistema")
        return
    Rut = input("Ingrese rut de usuario a modificar: ").strip().upper()
    if Rut not in clientes:
        print("Usuario no encontrado")
    else:
        print(f"Favor ingresa los nuevos datos para el Rut: {Rut}")
        nuevo_nombre = input("Ingresa nuevo Nombre: ")
        nuevo_telefono = input("Ingresa nuevo telefono: ")
        nuevo_mail = input("Ingresa nuevo mail: ")
        while True:
            nueva_vigencia = input("Ingresa nueva vigencia - S/N: ").strip().upper()
            if nueva_vigencia == "S" or nueva_vigencia == "N":
                break
            else:
                print("Error: Ingrese solamente 'S' para Sí o 'N' para No.")
        clientes[Rut] = {
            "nombre" : nuevo_nombre,
            "telefono" : nuevo_telefono,
            "mail" : nuevo_mail,
            "vigencia" : nueva_vigencia, 
        }
        print("Datos actualizados con exito")

def eliminar_cliente():
    if not clientes:
        print("No figuran clientes en el sistema")
        return
    
    Rut = input("Favor ingresa el Rut a eliminar: ").strip().upper()
    
    if Rut not in clientes:
        print("Usuario no encontrado")
    else:
        if Rut in reservas:
            asientos_viejos = reservas[Rut]
            for asiento in asientos_viejos:
                num = int(asiento)
                if num >= 1 and num <= 12:
                    sala_cine[0][num - 1] = asiento
                elif num >= 13 and num <= 24:
                    sala_cine[1][num - 13] = asiento
                elif num >= 25 and num <= 36:
                    sala_cine[2][num - 25] = asiento
                elif num >= 37 and num <= 48:
                    sala_cine[3][num - 37] = asiento
                elif num >= 49 and num <= 60:
                    sala_cine[4][num - 49] = asiento
                elif num >= 61 and num <= 72:
                    sala_cine[5][num - 61] = asiento           
            del reservas[Rut]
            print("Se eliminaron las reservas que tenía este cliente.")
        del clientes[Rut]
        print("Cliente Eliminado con éxito.")
                
def eliminar_reserva():
    if not reservas:
        print("No hay reservas en el sistema.")
        return
    Rut = input("Ingrese el RUT de la reserva a eliminar: ").strip().upper()
    if Rut not in reservas:
        print("Reserva no encontrada.")
    else:
        asientos_viejos = reservas[Rut]
        for asiento in asientos_viejos:
            num = int(asiento)
            if num >= 1 and num <= 12:
                sala_cine[0][num - 1] = asiento
            elif num >= 13 and num <= 24:
                sala_cine[1][num - 13] = asiento
            elif num >= 25 and num <= 36:
                sala_cine[2][num - 25] = asiento
            elif num >= 37 and num <= 48:
                sala_cine[3][num - 37] = asiento
            elif num >= 49 and num <= 60:
                sala_cine[4][num - 49] = asiento
            elif num >= 61 and num <= 72:
                sala_cine[5][num - 61] = asiento
                
        del reservas[Rut]
        print("Reserva eliminada y asientos liberados.")

def lista_reservas():
    if not reservas:
        print("No hay reservas registradas")
        return

    print("===== LISTA DE RESERVAS =====")
    for Rut, asientos in reservas.items():
        if Rut in clientes:
            nombre = clientes[Rut]["nombre"]
        else:
            nombre = "Cliente no encontrado"

        print(f"Rut: {Rut}")
        print(f"Nombre: {nombre}")
        print(f"Asientos: {asientos}")
        print("-----------------------------")

def imprimir_sala():
    print("\n" + " " * 18 + "[-----------------------PANTALLA-----------------------]\n")
    letras_pasillo = ["A", "B", "C", "D", "E", "F"]
    for i in range(len(sala_cine)):
        fila = sala_cine[i]
        letra = letras_pasillo[i]
        bloque1 = " ".join([f"[{asiento:>2}]" for asiento in fila[0:4]])
        bloque2 = " ".join([f"[{asiento:>2}]" for asiento in fila[4:8]])
        bloque3 = " ".join([f"[{asiento:>2}]" for asiento in fila[8:12]])
        print(f"Pasillo {letra}:  {bloque1}     {bloque2}     {bloque3}")
    print("\n")

def reserva_de_asientos():
    if not clientes:
        print("Debe haber clientes registrados para realizar una reserva.")
        return

    Rut = input("Ingrese el RUT del cliente que reserva: ").strip().upper()
    if Rut not in clientes:
        print("El cliente no está registrado.")
        return
    if clientes[Rut]["vigencia"] == "N":
        print("Error: El cliente NO está vigente. No puede reservar.")
        return
    if Rut in reservas:
        print("Este cliente ya tiene una reserva activa.")
        return

    while True:
        cantidad_texto = input("¿Cuántos asientos desea reservar?: ").strip()
        if cantidad_texto.isdigit() and int(cantidad_texto) > 0:
            cantidad = int(cantidad_texto)
            break
        else:
            print("Error: Ingrese una cantidad numérica válida (mayor a 0).")
    
    asientos_ocupados = obtener_asientos_reservados()
    asientos_nuevos = []
    for i in range(cantidad):
        while True:
            asiento = input(f"Seleccione el número de asiento ({i+1}/{cantidad}): ").strip()
            if not asiento.isdigit():
                print("Debe ingresar un número.")
                continue
                
            num = int(asiento)
            if num < 1 or num > 72:
                print("El asiento no existe en la sala. Pruebe del 1 al 72.")
                continue
            if asiento in asientos_ocupados or asiento in asientos_nuevos:
                print("El asiento ya está ocupado. Seleccione otro.")
                continue
                
            asientos_nuevos.append(asiento)
            break

    for asiento in asientos_nuevos:
        num = int(asiento)
        if num >= 1 and num <= 12:
            sala_cine[0][num - 1] = "X"
        elif num >= 13 and num <= 24:
            sala_cine[1][num - 13] = "X"
        elif num >= 25 and num <= 36:
            sala_cine[2][num - 25] = "X"
        elif num >= 37 and num <= 48:
            sala_cine[3][num - 37] = "X"
        elif num >= 49 and num <= 60:
            sala_cine[4][num - 49] = "X"
        elif num >= 61 and num <= 72:
            sala_cine[5][num - 61] = "X"
            
    reservas[Rut] = asientos_nuevos
    print("Reserva registrada con éxito.")

def modificar_reserva():
    if not reservas:
        print("No hay reservas registradas.")
        return
    Rut = input("Ingrese el RUT de la reserva a modificar: ").strip().upper()
    if Rut not in reservas:
        print("No se encontró reserva para ese RUT.")
        return
    while True:
        cantidad_texto = input("Ingrese la NUEVA cantidad de asientos: ").strip()
        if cantidad_texto.isdigit() and int(cantidad_texto) > 0:
            cantidad = int(cantidad_texto)
            break
        else:
            print("Error: Ingrese una cantidad numérica válida (mayor a 0).")   
    
    asientos_viejos = reservas[Rut]
    asientos_ocupados_otros = []
    for r_rut, r_asientos in reservas.items():
        if r_rut != Rut:
            asientos_ocupados_otros.extend(r_asientos)

    asientos_nuevos = []
    for i in range(cantidad):
        while True:
            asiento = input(f"Seleccione nuevo asiento ({i+1}/{cantidad}): ").strip()
            if not asiento.isdigit():
                print("Debe ser un número.")
                continue
                
            num = int(asiento)
            if num < 1 or num > 72:
                print("Asiento no existe. Pruebe del 1 al 72.")
                continue
            if asiento in asientos_ocupados_otros or asiento in asientos_nuevos:
                print("Asiento ya ocupado por otro usuario. Seleccione otro.")
                continue
                
            asientos_nuevos.append(asiento)
            break

    for asiento in asientos_viejos:
        num = int(asiento)
        if num >= 1 and num <= 12:
            sala_cine[0][num - 1] = asiento
        elif num >= 13 and num <= 24:
            sala_cine[1][num - 13] = asiento
        elif num >= 25 and num <= 36:
            sala_cine[2][num - 25] = asiento
        elif num >= 37 and num <= 48:
            sala_cine[3][num - 37] = asiento
        elif num >= 49 and num <= 60:
            sala_cine[4][num - 49] = asiento
        elif num >= 61 and num <= 72:
            sala_cine[5][num - 61] = asiento

    for asiento in asientos_nuevos:
        num = int(asiento)
        if num >= 1 and num <= 12:
            sala_cine[0][num - 1] = "X"
        elif num >= 13 and num <= 24:
            sala_cine[1][num - 13] = "X"
        elif num >= 25 and num <= 36:
            sala_cine[2][num - 25] = "X"
        elif num >= 37 and num <= 48:
            sala_cine[3][num - 37] = "X"
        elif num >= 49 and num <= 60:
            sala_cine[4][num - 49] = "X"
        elif num >= 61 and num <= 72:
            sala_cine[5][num - 61] = "X"

    reservas[Rut] = asientos_nuevos
    print("Reserva modificada con éxito.")

def menu_principal():
    while True:
        print("\n==== Bienvenido al sistema de reserva del cine ====")
        print("Seleccione una opcion")
        print("1. Crear cliente")
        print("2. Listar clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Reservar asientos")
        print("6. Modificar reserva")
        print("7. Eliminar reserva")
        print("8. Listar reservas")
        print("9. Imprimir sala")
        print("10. Salir")
    
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            crear_cliente() 
        elif opcion == "2":
            listar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            reserva_de_asientos()
        elif opcion == "6":
            modificar_reserva()
        elif opcion == "7":
            eliminar_reserva()
        elif opcion == "8":
            lista_reservas()
        elif opcion == "9":
            imprimir_sala()    
        elif opcion == "10":
            print("Saliendo del sistema, Adios!!!")
            break
        else:
            print("Opcion no valida, intentelo denuevo")

menu_principal()