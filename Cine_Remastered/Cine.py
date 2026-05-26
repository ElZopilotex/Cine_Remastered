clientes = {}
def crear_cliente():
    print("Ingresa tu Rut (Ejemplo: XX.XXX.XXX-K)")
    Rut = input("Rut: ")
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
        vigencia = input("Vigencia: ")
    clientes [Rut] ={
    "nombre" : nombre,
    "telefono" : telefono,
    "mail:" : correo,
    "vigencia" : vigencia
    }
    print("Cliente Registrado con exito")

def listar_cliente():
    if not clientes:
        print("No hay clientes registrados")
    else:
        print ("Lista de Clientes")
        for Rut, datos in clientes.item:
            print(f"RUT:{Rut}")

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
            eliminar_reserva()
        elif opcion == "5":
            reserva_de_asientos()
        elif opcion == "6":
            modificar_reserva()
        elif opcion == "7":
            eliminar_cliente()
        elif opcion == "8":
            lista_reservas()
        elif opcion == "9":
            imprimir_sala()    
        elif opcion == "10":
            print("Saliendo del sistema, Adios!!!")
        else:
            print("Opcion no valida, intentelo denuevo")

menu_principal()
