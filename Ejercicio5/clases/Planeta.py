###Clase Planeta###

from Ejercicio5.clases.Cuerpoceleste import CuerpoCeleste
from datetime import datetime
from math import pi

def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa_kg, radio_km, distancia_sol_km):
        super().__init__(nombre, masa_kg)
        self.__radio = 0.0
        self.__dist_sol = 0.0
        self.actualizar_radio(radio_km)
        self.actualizar_distancia_sol(distancia_sol_km)

    @property
    def radio_km(self): return self.__radio
    @property
    def distancia_sol_km(self): return self.__dist_sol

    def actualizar_radio(self, nuevo):
        if not (isinstance(nuevo, (int, float)) and nuevo > 0):
            raise ValueError("Radio debe ser > 0.")
        antes = self.__radio
        self.__radio = float(nuevo)
        if antes and antes != self.__radio:
            self.historial_eventos.append(f"{ahora()} | radio | {antes} -> {self.__radio}")

    def actualizar_distancia_sol(self, nueva):
        if not (isinstance(nueva, (int, float)) and nueva > 0):
            raise ValueError("Distancia debe ser > 0.")
        antes = self.__dist_sol
        self.__dist_sol = float(nueva)
        if antes and antes != self.__dist_sol:
            self.historial_eventos.append(f"{ahora()} | distancia_sol | {antes} -> {self.__dist_sol}")

    def calcular_densidad(self):
        # kg / km^3
        if self.__radio <= 0:
            raise ValueError("Radio inválido.")
        volumen = (4/3) * pi * (self.__radio ** 3)
        return self.masa_kg / volumen

    def comparar_distancia(self, otro):
        if not isinstance(otro, Planeta):
            raise TypeError("Comparar solo con Planeta.")
        if self.__dist_sol < otro.__dist_sol:
            return f"{self.nombre} está más cerca del sol que {otro.nombre}."
        if self.__dist_sol > otro.__dist_sol:
            return f"{otro.nombre} está más cerca del sol que {self.nombre}."
        return f"{self.nombre} y {otro.nombre} están a la misma distancia."
