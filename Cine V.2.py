clientes = {}
reservas = {}
sala_cine = [
                  #[---------------------PANTALLA---------------------]
    
    
             [ "1","2","3","4",     "5","6","7","8",    "9","10","11","12",],
             ["13","14","15","16", "17","18","19","20", "21","22","23","24",],
             ["25","26","27","28", "29","30","31","32", "33","34","35","36",],
             ["37","38","39","40", "41","42","43","44", "45","46","47","48",],
             ["49","50","51","52", "53","54","55","56", "57","58","59","60",],
             ["61","62","63","64", "65","66","67","68", "69","70","71","72",]
             ]

reservas = {}
def obtener_asientos_reservados():

    asientos_ocupados = []

    for lista_asientos in reservas.values():

        for asiento in lista_asientos:

            asientos_ocupados.append(asiento)

    return asientos_ocupados

def crear_cliente():
    print("Ingresa tu Rut (Ejemplo: XX.XXX.XXX-K)")
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
        print("Tiene vigencia? S / N")
        vigencia = input("Vigencia: ").strip().upper()
    clientes [Rut] ={
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
            print(f"RUT: {Rut}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Telefono: {datos['telefono']}")
            print(f"Mail: {datos['mail']}")
            print(f"Vigencia: {datos['vigencia']}")

def modificar_cliente():
    if not clientes:
        print("No se figuran clientes en el sistema")
        return
    Rut = input("Ingrese rut de usuario a modificar").strip().upper()
    if Rut not in clientes:
        print("Usuario no encontrado")
    else:
        print(f"Favor ingresa los nuevos datos para el Rut: {Rut}")
        nuevo_nombre = input("Ingresa nuevo Nombre: ")
        nuevo_telefono = input("Ingresa nuevo telefono: ")
        nuevo_mail = input("Ingresa nuevo mail: ")
        nueva_vigencia = input("Ingresa nueva vigencia - S/N: ")
    
    clientes [Rut] ={
        "nombre" : nuevo_nombre,
        "telefono" : nuevo_telefono,
        "mail" : nuevo_mail,
        "vigencia" : nueva_vigencia, 
    }
    print("Datos actualizados con exito")

def eliminar_cliente():
     if not clientes:
        print("No se figuran clientes en el sistema")
        return
     Rut = input("Favor ingresa el Rut a eliminar").strip().upper()
     if Rut not in clientes:
         print("Usuario no encontrado")
     else:
         del clientes [Rut]
         print("Cliente Eliminado con exito") 

def eliminar_reserva():
    if not reservas:
        print("No hay reservas registradas en el sistema.")
        return
    
    asiento_eliminar = input("Ingrese el número del asiento que desea liberar: ").strip()
    
    if asiento_eliminar not in reservas:
        print("Ese asiento no se encuentra reservado.")
    else:
        rut_cliente = reservas[asiento_eliminar]
        nombre_cliente = clientes.get(rut_cliente, {}).get("nombre", "Cliente Desconocido")
        
        del reservas[asiento_eliminar]
     
        for fila in sala_cine:
            if "X" in fila: 
                
                pass
        
        for i in range(len(sala_cine)):
            for j in range(len(sala_cine[i])):
                
                numero_original = str((i * 12) + (j + 1))
                if numero_original == asiento_eliminar:
                    sala_cine[i][j] = numero_original
        
        print(f"Reserva del asiento {asiento_eliminar} (Cliente: {nombre_cliente}) eliminada con éxito.")


def lista_reservas():
    if not reservas:
        print("No hay asientos reservados actualmente.")
    else:
        print("\n================ LISTA DE RESERVAS ================")
        print(f"{'Asiento':<10}{'RUT Cliente':<15}{'Nombre Cliente':<20}")
        print("-" * 45)
        for asiento, rut in reservas.items():
            
            nombre = clientes.get(rut, {}).get("nombre", "No registrado")
            print(f"{asiento:<10}{rut:<15}{nombre:<20}")
        print("===================================================\n")
def imprimir_sala():

    ocupados = obtener_asientos_reservados()

    print("\n" + " " * 18 + "[-----------------------PANTALLA-----------------------]\n")

    letras_pasillo = ["A", "B", "C", "D", "E", "F"]

    for i in range(len(sala_cine)):

        fila = sala_cine[i]
        letra = letras_pasillo[i]

        fila_mostrar = []

        for asiento in fila:

            if asiento in ocupados:
                fila_mostrar.append("[XX]")
            else:
                fila_mostrar.append(f"[{asiento:>2}]")

        bloque1 = " ".join(fila_mostrar[0:4])
        bloque2 = " ".join(fila_mostrar[4:8])
        bloque3 = " ".join(fila_mostrar[8:12])

        print(f"Pasillo {letra}:  {bloque1}     {bloque2}     {bloque3}")

    print("\n")


def reserva_de_asientos():

    Rut = input("Ingresa tu Rut: ").strip().upper()

    # Verificar si existe el cliente
    if Rut not in clientes:
        print("Cliente no registrado")
        return

    # Verificar vigencia
    if clientes[Rut]["vigencia"] != "S":
        print("Cliente no vigente")
        return

    imprimir_sala()

    print("Ingresa los asientos separados por coma")
    print("Ejemplo: 5,6,7")

    entrada = input("Asientos: ")

    lista_asientos = entrada.split(",")

    nuevos_asientos = []

    # Obtener asientos reservados
    ocupados = obtener_asientos_reservados()

    # Crear lista de asientos existentes
    asientos_existentes = []

    for fila in sala_cine:

        for asiento in fila:

            asientos_existentes.append(asiento)

    # Validar asientos
    for asiento in lista_asientos:

        asiento = asiento.strip()

        # Validar existencia
        if asiento not in asientos_existentes:
            print(f"El asiento {asiento} no existe")
            return

        # Validar disponibilidad
        if asiento in ocupados:
            print(f"El asiento {asiento} ya está reservado")
            return

        nuevos_asientos.append(asiento)

    # Guardar reserva
    reservas[Rut] = nuevos_asientos

    print("Reserva realizada con éxito")


def modificar_reserva():

    Rut = input("Ingresa el Rut: ").strip().upper()

    # Verificar si tiene reserva
    if Rut not in reservas:
        print("El cliente no tiene reservas")
        return

    print(f"Reserva actual: {reservas[Rut]}")

    imprimir_sala()

    print("Ingresa los nuevos asientos separados por coma")
    print("Ejemplo: 10,11,12")

    entrada = input("Nuevos asientos: ")

    nuevos = entrada.split(",")

    nuevos_asientos = []

    # Lista de asientos existentes
    asientos_existentes = []

    for fila in sala_cine:

        for asiento in fila:

            asientos_existentes.append(asiento)

    # Asientos ocupados por OTROS clientes
    ocupados = []

    for rut_cliente, lista in reservas.items():

        if rut_cliente != Rut:

            for asiento in lista:

                ocupados.append(asiento)

    # Validaciones
    for asiento in nuevos:

        asiento = asiento.strip()

        # Validar existencia
        if asiento not in asientos_existentes:
            print(f"El asiento {asiento} no existe")
            return

        # Validar disponibilidad
        if asiento in ocupados:
            print(f"El asiento {asiento} ya está ocupado")
            return

        nuevos_asientos.append(asiento)

    # Actualizar reserva
    reservas[Rut] = nuevos_asientos

    print("Reserva modificada con éxito")

def eliminar_reserva():

    Rut = input("Ingresa el Rut: ").strip().upper()

    if Rut not in reservas:
        print("No existe reserva para ese cliente")
        return

    del reservas[Rut]

    print("Reserva eliminada con éxito")


def lista_reservas():

    if not reservas:
        print("No hay reservas registradas")
        return

    print("===== LISTA DE RESERVAS =====")

    for Rut, asientos in reservas.items():

        nombre = clientes[Rut]["nombre"]

        print(f"Rut: {Rut}")
        print(f"Nombre: {nombre}")
        print(f"Asientos: {asientos}")
        print("-----------------------------")

def menu_principal():
   while True:
        print("==== Bienvenido al sistema de reserva del cine ====")

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
    
        opcion = input("Seleccione una opcion: ")


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
