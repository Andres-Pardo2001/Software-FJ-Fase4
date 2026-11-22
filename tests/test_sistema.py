"""Pruebas unitarias básicas del sistema Software FJ."""
import unittest
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva, EstadoReserva
from excepciones import DatosInvalidosError, EstadoReservaError, ServicioNoDisponibleError

class TestSoftwareFJ(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("C1", "Ana Torres", "ana@test.com", "3001234567")
        self.sala = ReservaSala("S1", "Sala A", 10000, 8)

    def test_cliente_correo_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente("C2", "Luis", "correo", "3001234567")

    def test_calculo_con_impuesto_descuento(self):
        self.assertEqual(self.sala.calcular_costo(2, impuesto=0.19, descuento=0.10), 21420.0)

    def test_reserva_confirmar_y_procesar(self):
        reserva = Reserva("R1", self.cliente, self.sala, 2)
        reserva.confirmar()
        self.assertEqual(reserva.estado, EstadoReserva.CONFIRMADA)
        reserva.procesar()
        self.assertEqual(reserva.estado, EstadoReserva.PROCESADA)

    def test_no_procesar_pendiente(self):
        reserva = Reserva("R2", self.cliente, self.sala, 1)
        with self.assertRaises(EstadoReservaError):
            reserva.procesar()

    def test_servicio_no_disponible(self):
        equipo = AlquilerEquipo("E1", "Portátil", 20000, 2, disponible=False)
        with self.assertRaises(ServicioNoDisponibleError):
            Reserva("R3", self.cliente, equipo, 1)

    def test_asesoria_polimorfica(self):
        asesoria = AsesoriaEspecializada("A1", "Consultoría", 50000, "Sistemas")
        self.assertIn("Sistemas", asesoria.describir())

if __name__ == "__main__":
    unittest.main()
