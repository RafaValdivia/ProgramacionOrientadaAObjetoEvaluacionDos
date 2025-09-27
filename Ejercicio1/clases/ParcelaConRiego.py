#Clase Parcela con riego - Clase Herencia

from datetime import datetime

from Ejercicio1.clases import Parcela

class ParcelaConRiego(Parcela):
    def __init__(self, id_parcela, superficie_ha, cultivo_actual=None):
        super().__init__(id_parcela, superficie_ha, cultivo_actual)
        self.litros_disponibles = 0
        self.tasa_riego_l_ha = 0
        self.umbral_min_litros = 0
        self.estado_riego = "inhabilitado"
        self.eventos_riego = []

    def configurar_tasa(self, l_ha):
        self.tasa_riego_l_ha = l_ha

    def configurar_umbral(self, litros):
        self.umbral_min_litros = litros

    def habilitar_riego(self):
        self.estado_riego = "habilitado"

    def cargar_agua(self, litros):
        self.litros_disponibles += litros
        self._registrar_evento_riego(f"Se cargaron {litros} litros")

    def regar_automatico(self, modo="estricto"):
        if self.estado != "activa" or self.estado_riego != "habilitado":
            print("No se puede regar: parcela inactiva o riego inhabilitado")
            return

        demanda = self.superficie_ha * self.tasa_riego_l_ha

        if self.litros_disponibles < self.umbral_min_litros:
            print("No se puede regar: no se cumple umbral mínimo")
            return

        if modo == "estricto" and self.litros_disponibles >= demanda:
            self.litros_disponibles -= demanda
            self._registrar_evento_riego(f"Riego estricto: {demanda} litros aplicados")
        elif modo == "parcial":
            aplicado = min(self.litros_disponibles, demanda)
            self.litros_disponibles -= aplicado
            self._registrar_evento_riego(f"Riego parcial: {aplicado} litros aplicados")

    def _registrar_evento_riego(self, descripcion):
        self.eventos_riego.append({
            "fecha": datetime.now(),
            "descripcion": descripcion,
            "saldo": self.litros_disponibles
        })

    def mostrar_eventos_riego(self):
        for e in self.eventos_riego:
            print(f"[{e['fecha']}] {e['descripcion']} (Saldo: {e['saldo']} L)")
