###Clase Publicacion###

from datetime import datetime

class Publicacion:
    def __init__(self, id_publicacion: int, titulo: str, año: int):
        self.id_publicacion = id_publicacion
        self._titulo = None
        self._año = None
        self.historial_eventos = []

        self.actualizar_titulo(titulo)
        self.actualizar_año(año)

    @property
    def titulo(self):
        return self._titulo

    @property
    def año(self):
        return self._año

    def actualizar_titulo(self, nuevo_titulo: str):
        if not nuevo_titulo or not nuevo_titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        anterior = self._titulo
        self._titulo = nuevo_titulo.strip()
        if anterior != self._titulo:
            self._registrar_cambio("titulo", anterior, self._titulo)

    def actualizar_año(self, nuevo_año: int):
        if nuevo_año < 1450:
            raise ValueError("El año debe ser ≥ 1450 (imprenta moderna).")
        anterior = self._año
        self._año = int(nuevo_año)
        if anterior != self._año:
            self._registrar_cambio("año", anterior, self._año)

    def _registrar_cambio(self, campo, anterior, nuevo):
        self.historial_eventos.append({
            "fecha": datetime.now(),
            "campo": campo,
            "anterior": anterior,
            "nuevo": nuevo
        })

    def mostrar_historial(self):
        for e in self.historial_eventos:
            print(f"[{e['fecha']:%Y-%m-%d %H:%M:%S}] {e['campo']}: {e['anterior']} -> {e['nuevo']}")
