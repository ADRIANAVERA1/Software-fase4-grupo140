import datetime
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteError, ServicioError, ReservaError

def registrar_log(error):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] {str(error)}\n")

# --- NUEVA FUNCIÓN DE SIMULACIÓN ---
def ejecutar_simulacion():
    print("\n" + "="*40)
    print("  INICIANDO SIMULACIÓN DE 10 CASOS  ")
    print("="*40)
    
    # Lista de tuplas: (Nombre, Documento, TipoServicio, Horas)
    casos = [
        ("Adriana Vera", "1012345", "1", 3),     # Caso 1: Éxito Sala
        ("Carlos Ruiz", "1023456", "2", 2),      # Caso 2: Éxito Equipo
        ("", "1034567", "1", 2),                 # Caso 3: Error Nombre vacío
        ("Marta Sol", "ABC999", "3", 4),         # Caso 4: Éxito Asesoría
        ("Jose Perez", "1045678", "5", 2),       # Caso 5: Error Servicio inválido
        ("Luis Leon", "1056789", "1", -5),       # Caso 6: Error Horas negativas
        ("Ana Gomez", "1067890", "2", 0),        # Caso 7: Caso borde 0 horas
        (None, "1078901", "1", 2),               # Caso 8: Error Nombre Nulo
        ("Pedro Paz", "", "3", 1),               # Caso 9: Error Documento vacío
        ("User Test", "1090123", "1", 1)         # Caso 10: Éxito final
    ]

    for i, (nom, doc, serv, hrs) in enumerate(casos, 1):
        try:
            print(f"Caso {i}: ", end="")
            obj_cliente = Cliente(nom, doc)
            
            if serv == "1": obj_serv = ReservaSala("Sala VIP", 50000)
            elif serv == "2": obj_serv = AlquilerEquipo("Equipo", 30000)
            elif serv == "3": obj_serv = AsesoriaEspecializada("Asesoria", 60000)
            else: raise ServicioError("Tipo de servicio no existe")
            
            obj_reserva = Reserva(obj_cliente, obj_serv, hrs)
            obj_reserva.confirmar()
            print(f"ÉXITO -> Total: {obj_reserva.procesar()}")
            
        except (ClienteError, ServicioError, ReservaError, Exception) as e:
            registrar_log(f"Simulación Caso {i}: {e}")
            print(f"CONTROLADO -> {e}")

    print("\n" + "="*40)
    print("      FIN DE LA SIMULACIÓN      ")
    print("="*40 + "\n")

# --- INICIO DEL PROGRAMA ---
print(" SISTEMA SOFTWARE FJ ")
ejecutar_simulacion() # Primero corre los 10 casos automáticamente

while True:
    try:
        print("\n MENÚ PRINCIPAL (Modo Manual)")
        print("1. Crear reserva")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            documento = input("Ingrese el documento: ")
            cliente = Cliente(nombre, documento)

            print("\nSERVICIOS DISPONIBLES")
            print("1. Sala VIP")
            print("2. Alquiler Equipo")
            print("3. Asesoría")

            op_servicio = input("Seleccione el servicio: ")
            horas = int(input("Ingrese horas de uso: "))

            if op_servicio == "1":
                servicio = ReservaSala("Sala VIP", 50000)
            elif op_servicio == "2":
                servicio = AlquilerEquipo("Equipo", 30000)
            elif op_servicio == "3":
                servicio = AsesoriaEspecializada("Asesoria", 60000)
            else:
                raise ServicioError("Servicio inválido")

            reserva = Reserva(cliente, servicio, horas)
            reserva.confirmar()

            print("\n✔ RESERVA EXITOSA")
            print(f"Cliente: {cliente}")
            print(f"Estado: {reserva.estado}")
            print(f"Total: {reserva.procesar()}")

        elif opcion == "2":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")

    except Exception as e:
        registrar_log(f"Error en Menú: {e}")
        print(f" Error: {e}")
