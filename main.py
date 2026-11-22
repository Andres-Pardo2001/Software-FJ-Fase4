"""Demostración de Software FJ: más de 10 operaciones y manejo de excepciones."""
import logging
from pathlib import Path
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import SoftwareFJError

RUTA_LOG = Path(__file__).parent / "logs" / "sistema.log"
RUTA_LOG.parent.mkdir(exist_ok=True)
logging.basicConfig(
    filename=RUTA_LOG, level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger("SoftwareFJ")

def ejecutar_operacion(numero, descripcion, funcion):
    """Aísla cada operación para que un error no detenga el programa."""
    print(f"\nOPERACIÓN {numero}: {descripcion}")
    try:
        resultado = funcion()
    except (SoftwareFJError, ValueError, TypeError) as error:
        logger.exception("Error controlado en operación %s: %s", numero, error)
        print(f"Error controlado: {error}")
    except Exception as error:
        logger.exception("Error inesperado en operación %s", numero)
        print(f"Error inesperado registrado: {error}")
    else:
        logger.info("Operación %s realizada correctamente", numero)
        print(resultado)
    finally:
        print("Fin de la operación.")

def main():
    clientes = []
    servicios = []
    reservas = []

    # 1. Registro válido de cliente.
    ejecutar_operacion(1, "Registrar cliente válido", lambda: (
        clientes.append(Cliente("C001", "Laura Gómez", "laura@email.com", "3001234567"))
        or clientes[-1].describir()
    ))

    # 2. Registro inválido: correo incorrecto.
    ejecutar_operacion(2, "Registrar cliente con correo inválido",
        lambda: clientes.append(Cliente("C002", "Carlos Ruiz", "correo-invalido", "3115556677")))

    # 3. Registro de segundo cliente válido.
    ejecutar_operacion(3, "Registrar segundo cliente válido", lambda: (
        clientes.append(Cliente("C003", "Andrés Pérez", "andres@email.com", "3207654321"))
        or clientes[-1].describir()
    ))

    # 4. Crear servicio de sala.
    ejecutar_operacion(4, "Crear sala de reuniones", lambda: (
        servicios.append(ReservaSala("S001", "Sala Ejecutiva", 50000, 12))
        or servicios[-1].describir()
    ))

    # 5. Crear servicio con tarifa inválida.
    ejecutar_operacion(5, "Crear servicio con tarifa negativa",
        lambda: servicios.append(AlquilerEquipo("S002", "Proyector", -1000, 2)))

    # 6. Crear alquiler de equipo.
    ejecutar_operacion(6, "Crear alquiler de equipos", lambda: (
        servicios.append(AlquilerEquipo("S003", "Proyector HD", 25000, 5))
        or servicios[-1].describir()
    ))

    # 7. Crear asesoría.
    ejecutar_operacion(7, "Crear asesoría especializada", lambda: (
        servicios.append(AsesoriaEspecializada("S004", "Asesoría TI", 80000, "Tecnología"))
        or servicios[-1].describir()
    ))

    # 8. Consultar y calcular costo con impuesto.
    ejecutar_operacion(8, "Calcular costo de sala con impuesto",
        lambda: f"Costo con impuesto: ${servicios[0].calcular_costo(2, impuesto=0.19):,.2f}")

    # 9. Crear reserva correcta.
    ejecutar_operacion(9, "Crear reserva de sala", lambda: (
        reservas.append(Reserva("R001", clientes[0], servicios[0], 2))
        or reservas[-1].describir()
    ))

    # 10. Intentar una reserva con duración inválida.
    ejecutar_operacion(10, "Intentar reserva con duración inválida",
        lambda: Reserva("R002", clientes[0], servicios[0], 30))

    # 11. Confirmar reserva.
    ejecutar_operacion(11, "Confirmar reserva R001", lambda: reservas[0].confirmar())

    # 12. Procesar reserva confirmada.
    ejecutar_operacion(12, "Procesar reserva R001", lambda: reservas[0].procesar())

    # 13. Intentar cancelar una reserva ya procesada.
    ejecutar_operacion(13, "Cancelar reserva procesada",
        lambda: reservas[0].cancelar())

    # 14. Encadenamiento de excepciones.
    def operacion_encadenada():
        try:
            int("dato-no-numerico")
        except ValueError as error:
            raise SoftwareFJError("No fue posible convertir el dato recibido.") from error
    ejecutar_operacion(14, "Demostrar encadenamiento de excepciones", operacion_encadenada)

    print("\nResumen:")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")
    print(f"Los eventos y errores se registraron en: {RUTA_LOG}")
    logger.info("Ejecución de demostración finalizada.")

if __name__ == "__main__":
    main()
