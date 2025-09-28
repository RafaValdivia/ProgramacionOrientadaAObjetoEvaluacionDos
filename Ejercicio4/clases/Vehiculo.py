###Clase Vehiculo###

class Vehiculo:
    _id = 0
    def __init__(self, patente, peso):
        Vehiculo._id += 1
        self.id = Vehiculo._id
        if not isinstance(patente, str) or patente.strip() == "":
            raise ValueError("Patente inválida")
        if peso <= 0:
            raise ValueError("El peso debe ser > 0")
        self.patente = patente.strip()
        self.peso = float(peso)

    def actualizar_peso(self, nuevo_peso):
        if nuevo_peso <= 0:
            raise ValueError("El peso debe ser > 0")
        self.peso = float(nuevo_peso)
