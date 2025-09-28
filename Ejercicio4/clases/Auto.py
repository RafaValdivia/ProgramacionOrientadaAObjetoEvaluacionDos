###Clase Auto###

from Ejercicio4.clases import Vehiculo

class Auto(Vehiculo):
    def __init__(self, patente, peso, asientos):
        super().__init__(patente, peso)
        if not isinstance(asientos, int) or asientos < 2:
            raise ValueError("Asientos debe ser un entero >= 2")
        self.asientos = asientos
        self.ocupantes = 0

    def subir(self, n):
        if n < 1:
            raise ValueError("n debe ser >= 1")
        if self.ocupantes + n > self.asientos:
            raise ValueError("No hay asientos suficientes")
        self.ocupantes += n

    def bajar(self, n):
        if n < 1:
            raise ValueError("n debe ser >= 1")
        if self.ocupantes - n < 0:
            raise ValueError("No puede quedar negativo")
        self.ocupantes -= n

    def set_asientos(self, nuevo):
        if not isinstance(nuevo, int) or nuevo < 2:
            raise ValueError("Asientos debe ser >= 2")
        if nuevo < self.ocupantes:
            raise ValueError("No puede ser menor que los ocupantes actuales")
        self.asientos = nuevo
