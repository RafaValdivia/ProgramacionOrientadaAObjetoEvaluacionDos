###Clase Cuerpo Celeste###

from datetime import datetime
from math import pi

def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class CuerpoCeleste:
    _id = 0
    def __init__(self, nombre, masa_kg):
        CuerpoCeleste._id += 1
        self.__id = CuerpoCeleste._id
        self.__nombre = ""
        self.__masa = 0.0
        self.__hist = []

        self.actualizar_nombre(nombre)
        self.actualizar_masa(masa_kg)
        self.__hist.append(f"{ahora()} | creacion | id={self.__id}")

    @property
    def id_celeste(self): return self.__id
    @property
    def nombre(self): return self.__nombre
    @property
    def masa_kg(self): return self.__masa
    @property
    def historial_eventos(self): return list(self.__hist)

    # operaciones
    def actualizar_nombre(self, nuevo):
        if not isinstance(nuevo, str) or nuevo.strip() == "":
            raise ValueError("Nombre vacío.")
        antes = self.__nombre
        self.__nombre = nuevo.strip()
        if antes and antes != self.__nombre:
            self.__hist.append(f"{ahora()} | nombre | {antes} -> {self.__nombre}")

    def actualizar_masa(self, nueva):
        if not (isinstance(nueva, (int, float)) and nueva > 0):
            raise ValueError("Masa debe ser > 0.")
        antes = self.__masa
        self.__masa = float(nueva)
        if antes and antes != self.__masa:
            self.__hist.append(f"{ahora()} | masa | {antes} -> {self.__masa}")

    # ficha simple
    def consultar_ficha(self):
        ult_masa = next((h for h in reversed(self.__hist) if " | masa | " in h), None)
        fecha_ult_masa = ult_masa.split(" | ")[0] if ult_masa else "sin registro"
        mods = len(self.__hist) - 1  # sin contar "creacion"
        return {
            "id_celeste": self.__id,
            "nombre": self.__nombre,
            "masa_kg": self.__masa,
            "ultima_actualizacion_masa": fecha_ult_masa,
            "modificaciones": mods,
            "ultimo_evento": self.__hist[-1]
        }
