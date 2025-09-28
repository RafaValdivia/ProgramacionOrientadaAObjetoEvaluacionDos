###Clase Actividad###

class Actividad:
    _autoid = 0

    def __init__(self, nombre, duracion):
        Actividad._autoid += 1
        self.id = Actividad._autoid
        self.nombre = nombre
        if duracion < 1:
            raise ValueError("Duración mínima = 1")
        self.duracion = duracion
        self.historial = []

    def actualizar_nombre(self, nuevo):
        if nuevo.strip() == "":
            raise ValueError("Nombre no puede ser vacío")
        antes = self.nombre
        self.nombre = nuevo
        self.historial.append(f"Nombre: {antes} -> {nuevo}")

    def actualizar_duracion(self, nueva):
        if nueva < 1:
            raise ValueError("Duración mínima = 1")
        antes = self.duracion
        self.duracion = nueva
        self.historial.append(f"Duración: {antes} -> {nueva}")

    def descripcion(self):
        return f"Actividad {self.nombre} ({self.duracion} min)"
