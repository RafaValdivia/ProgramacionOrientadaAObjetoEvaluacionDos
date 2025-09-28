#Clase Parcela - Clase Base

from datetime import datetime

class Parcela:
    def __init__(self, id_parcela, superficie_ha, cultivo_actual=None):
        self.id_parcela = id_parcela
        self.superficie_ha = round(superficie_ha, 2)
        self.cultivo_actual = cultivo_actual if cultivo_actual else ""
        self.estado = "activa"
        self.historial_eventos = []

    def actualizar_cultivo(self, nuevo_cultivo):
        if nuevo_cultivo:
            self.cultivo_actual = nuevo_cultivo
            self._registrar_evento(f"Cambio de cultivo a {nuevo_cultivo}")

    def _registrar_evento(self, descripcion):
        self.historial_eventos.append({
            "fecha": datetime.now(),
            "descripcion": descripcion
        })

    def mostrar_eventos(self):
        for e in self.historial_eventos:
            print(f"[{e['fecha']}] {e['descripcion']}")
