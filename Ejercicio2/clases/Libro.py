###Clase Libro###

from datetime import datetime
from Ejercicio2.clases import Publicacion


class Libro(Publicacion):
    def __init__(self, id_publicacion: int, titulo: str, año: int, paginas_totales: int):
        super().__init__(id_publicacion, titulo, año)
        if paginas_totales <= 0:
            raise ValueError("paginas_totales debe ser > 0.")
        self._paginas_totales = int(paginas_totales)  
        self._paginas_leidas = 0
        self.eventos_lectura = []   

    @property
    def paginas_totales(self):
        return self._paginas_totales

    @property
    def paginas_leidas(self):
        return self._paginas_leidas

    def leer(self, paginas: int):
        """Incrementa páginas leídas cumpliendo reglas."""
        if paginas <= 0:
            raise ValueError("No se pueden leer páginas negativas ni cero.")
        restantes = self._paginas_totales - self._paginas_leidas
        if paginas > restantes:
            raise ValueError("No puedes leer más páginas de las que faltan.")

        antes = self._paginas_leidas
        self._paginas_leidas += paginas
        despues = self._paginas_leidas
        progreso = self.consultar_progreso()

        self._registrar_evento_lectura(antes, paginas, despues, progreso)

    def consultar_progreso(self) -> float:
        """Devuelve % de progreso redondeado a 2 decimales."""
        return round((self._paginas_leidas / self._paginas_totales) * 100, 2)

    def __setattr__(self, name, value):
        if hasattr(self, "_paginas_totales") and name == "_paginas_totales":
            raise AttributeError("No se puede modificar 'paginas_totales' luego de creado el libro.")
        if hasattr(self, "_paginas_leidas") and name == "_paginas_leidas":
            pass
        super().__setattr__(name, value)

    def _registrar_evento_lectura(self, antes, aplicadas, despues, progreso):
        self.eventos_lectura.append({
            "fecha": datetime.now(),
            "paginas_leidas_antes": antes,
            "paginas_aplicadas": aplicadas,
            "paginas_leidas_despues": despues,
            "progreso_pct": progreso
        })

    def mostrar_eventos_lectura(self):
        for e in self.eventos_lectura:
            print(
                f"[{e['fecha']:%Y-%m-%d %H:%M:%S}] "
                f"Lectura +{e['paginas_aplicadas']} pág. "
                f"({e['paginas_leidas_antes']}→{e['paginas_leidas_despues']}) "
                f"- Progreso: {e['progreso_pct']}%"
            )
