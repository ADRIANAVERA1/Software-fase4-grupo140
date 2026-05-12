import datetime
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorSoftwareFJ, ClienteError, ServicioError, ReservaError

def registrar_log(evento):
    try:
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.write(f"[{fecha}] {evento}\n")
    except Exception as e:
        print(f"Error al escribir en el log: {e}")

def ejecutar_simulacion():
    print("\n--- INICIANDO SIMULACIÓN OBLIGATORIA (10 CASOS) ---")
    casos = [
        ("Juan Perez", "1012345", "1", 2),
        ("", "1023456", "1", 2),
        ("Ana Gomez", "ABC1234", "2", 3),
        ("Luis Rios", "1034567", "2", 5),
        ("Marta Paz", "1045678", "3", 0),
        ("Pedro Jara", "1056789", "4", 2),
        ("Jose Cano", "1067890", "1", -1),
        ("Clara Luz", "1078901", "3", 4),
        (None, "1089012", "2", 2),
        ("Final Test", "1090123", "1", 1)
    ]

    for i, (nom, doc, serv_tipo, hrs) in enumerate(casos, 1):
        try:
            print(f"Operación {i}: ", end="")
            c = Cliente(nom, doc)
            
            if serv_tipo == "1": s = ReservaSala("Sala VIP", 50000)
            elif serv_tipo == "2": s = AlquilerEquipo("Portátil", 30000)
            elif serv_tipo == "3": s = AsesoriaEspecializada("Asesoría Java", 60000)
            else: raise ServicioError("Tipo de servicio no reconocido")
            
            r = Reserva(c, s, hrs)
            print(r.procesar())
            
        except ErrorSoftwareFJ as e:
            registrar_log(f"Caso {i}: {e}")
            print(f"Controlado: {e}")
        except Exception as e:
            registrar_log(f"Caso {i} (Crítico): {e}")
            print(f"Falla: {e}")

print(" SISTEMA SOFTWARE FJ ")
ejecutar_simulacion()

while True:
    try:
        print("\n MENÚ PRINCIPAL ")
        print("1. Crear reserva")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            documento = input("Ingrese el documento: ")
            cliente = Cliente(nombre, documento)

            print("\nSERVICIOS DISPONIBLES")
            print("1. Sala VIP: 50.000 COP/hora")
            print("2. Alquiler Equipo: 30.000 COP/hora + 2.000 COP cargo fijo")
            print("3. Asesoría: 60.000 COP/hora + 15% adicional")

            op_servicio = input("Seleccione el servicio: ")
            horas_input = input("Ingrese horas de uso: ")
            horas = int(horas_input)

            if op_servicio == "1":
                servicio = ReservaSala("Sala VIP", 50000)
            elif op_servicio == "2":
                servicio = AlquilerEquipo("Equipo", 30000)
            elif op_servicio == "3":
                servicio = AsesoriaEspecializada("Asesoría", 60000)
            else:
                raise ServicioError("Opción de servicio no válida")

            reserva = Reserva(cliente, servicio, horas)
            print("\n" + reserva.procesar())

        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

    except ErrorSoftwareFJ as e:
        registrar_log(f"Error en Menú: {e}")
        print(f"\n[ERROR CONTROLADO] {e}")
    except ValueError:
        print("\n[ERROR] Las horas deben ser un número entero.")
    except Exception as e:
        registrar_log(f"Error Inesperado: {e}")
        print(f"\n[ERROR CRÍTICO] {e}")