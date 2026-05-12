import datetime
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorSoftwareFJ, ClienteError, ServicioError, ReservaError

def registrar_log(error):
    with open("logs.txt", "a") as archivo:
        archivo.write(str(error) + "\n")

print(" SISTEMA SOFTWARE FJ ")

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
                print("Servicio inválido")
                continue

            reserva = Reserva(cliente, servicio, horas)
            reserva.confirmar()

            print("\n✔ RESERVA EXITOSA")
            print("Cliente:", cliente)
            print("Estado:", reserva.estado)
            print("Total:", reserva.procesar())

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
        registrar_log(e)
        print(" Error ", e)
