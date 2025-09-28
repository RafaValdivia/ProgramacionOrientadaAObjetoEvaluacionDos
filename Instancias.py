##### Instancias #####

##### Ejercicio 1 - Gestión de parcelas con riego automatizado #####

from Ejercicio1.clases import ParcelaConRiego

if __name__ == "__main__":
    parcela1 = ParcelaConRiego(1, 50, "Trigo")
    parcela1.configurar_tasa(150)
    parcela1.configurar_umbral(2000)
    parcela1.habilitar_riego()
    parcela1.cargar_agua(3000)
    parcela1.regar_automatico("estricto")
    parcela1.mostrar_eventos_riego()
    
##### Ejercicio 2 - Club de lectura #####

from Ejercicio2.clases import Libro, Publicacion

if __name__ == "__main__":
    #Instancia de Publicación
    print("=== PUBLICACIÓN ===")
    publicacion1 = Publicacion(1, "Revista Ciencia", 2000)
    publicacion1.actualizar_titulo("Revista Ciencia y Tecnología")
    publicacion1.actualizar_año(2005)
    publicacion1.mostrar_historial()

    #Instancia de Libro
    print("\n=== LIBRO ===")
    libro1 = Libro(2, "El Principito", 1943, 100)
    libro1.leer(30)   # leer 30 páginas
    libro1.leer(20)   # leer 20 páginas más
    print("Progreso:", libro1.consultar_progreso(), "%")

    # Cambiar el año
    libro1.actualizar_año(1945)

    # Mostrar historial y eventos de lectura
    print("\nHistorial del libro:")
    libro1.mostrar_historial()

    print("\nEventos de lectura:")
    libro1.mostrar_eventos_lectura()

##### Ejercicio 3 - Registro de actividades fisicas #####

from Ejercicio3.clases import Actividad, Carrera

if __name__ == "__main__":
    #Instancia Actividad
    yoga = Actividad("Yoga", 60)
    print(yoga.descripcion())

    #Instancia Carrera
    c = Carrera("10K", 25)
    c.registrar_distancia(10)
    print(c.descripcion())        # 25/10 = 2.5
    c.actualizar_duracion(25)
    print(c.descripcion())        # ahora 35/10 = 3.5

    print("\nHistorial:")
    for h in c.historial:
        print("-", h)
        
##### Ejercicio 4 - Registro y gestion de vehiculos #####

from Ejercicio4.clases import Auto, Vehiculo

if __name__ == "__main__":
    v = Vehiculo("ABCD12", 1200)
    v.actualizar_peso(1300)
    a = Auto("XYZD34", 1000, 5)
    a.subir(3); a.bajar(1); a.set_asientos(6)
    print(v.id, v.patente, v.peso)
    print(a.id, a.patente, a.peso, a.asientos, a.ocupantes)
    
### Ejercicio 5 - Catalogo de Planetas ###

from Ejercicio5.clases import Planeta
from Ejercicio5.clases.Cuerpoceleste import CuerpoCeleste

if __name__ == "__main__":
    # Cuerpo celeste
    estrella = CuerpoCeleste("Estrella X", 2e30)
    print(estrella.consultar_ficha())

    # Tierra y Marte
    tierra = Planeta("Tierra", 5.97e24, 6371, 149_600_000)
    marte  = Planeta("Marte", 6.42e23, 3389, 227_900_000)
    print("Densidad Tierra:", round(tierra.calcular_densidad(), 2))
    print(tierra.comparar_distancia(marte))

    # Rechazos
    try: Planeta("Fallo", 1e20, 0, 1e6)
    except Exception as e: print("OK radio:", e)
    try: Planeta("Fallo2", 1e20, 100, -5)
    except Exception as e: print("OK distancia:", e)

    # Actualizar masa (queda en historial)
    tierra.actualizar_masa(5.98e24)
    print("Último evento:", tierra.historial_eventos[-1])

    # Intento de cambio directo (debe fallar)
    try: tierra.masa_kg = 1
    except AttributeError as e: print("Bloqueado masa:", e)
    try: tierra.radio_km = 1
    except AttributeError as e: print("Bloqueado radio:", e)
    try: tierra.distancia_sol_km = 1
    except AttributeError as e: print("Bloqueado distancia:", e)