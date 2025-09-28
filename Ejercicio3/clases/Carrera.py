###Clase Carrera###

from Ejercicio3.clases import Actividad

class Carrera(Actividad):
    def __init__(self, nombre, duracion):
        super().__init__(nombre, duracion)
        self.distancia = 0
        self.eventos = []

    def registrar_distancia(self, nueva):
        if nueva <= 0:
            raise ValueError("Distancia debe ser >0")
        if self.distancia > 0 and nueva < self.distancia:
            raise ValueError("No se puede disminuir la distancia")
        antes = self.distancia
        self.distancia = nueva
        self.eventos.append(f"Distancia: {antes} -> {nueva}")
        self.historial.append(f"Distancia: {antes} -> {nueva}")

    def calcular_ritmo(self):
        if self.distancia == 0:
            raise ValueError("No hay distancia registrada")
        return round(self.duracion / self.distancia, 2)

    def descripcion(self):
        if self.distancia == 0:
            return f"Carrera {self.nombre} ({self.duracion} min)"
        else:
            return f"Carrera {self.nombre} ({self.duracion} min, {self.distancia} km, {self.calcular_ritmo()} min/km)"
