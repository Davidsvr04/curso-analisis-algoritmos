"""Experimentos de medicion: lista enlazada vs. tabla hash.

Experimento A: tiempo medio de busqueda de guias inexistentes frente
al numero de guias almacenadas (n), con la tabla usando m primo
cercano a n / 2 (factor de carga alrededor de 2).

Experimento B: con n fijo, tiempo medio de busqueda de guias
inexistentes en la tabla frente al factor de carga (alfa), variando m.
"""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANOS_N = [100, 500, 1000, 5000, 20000, 50000]
BUSQUEDAS_POR_MEDICION = 200
REPETICIONES = 3
N_FIJO_EXPERIMENTO_B = 20000
ALFAS = [0.5, 1, 4, 10]
SEMILLA_GUIAS = 1
SEMILLA_INEXISTENTES = 7
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias_existentes(
    n: int, semilla: int = SEMILLA_GUIAS
) -> list[int]:
    """Genera n guias de diez digitos, distintas entre si.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla del generador, para que el experimento sea
            reproducible.

    Returns:
        Lista de n enteros distintos entre 10**9 y 10**10 - 1.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def es_primo(n: int) -> bool:
    """Determina si n es primo por division de prueba.

    Args:
        n: numero entero a evaluar.

    Returns:
        True si n es primo, False en caso contrario.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def primo_cercano(objetivo: int) -> int:
    """Encuentra el primo mas cercano a objetivo, buscando hacia afuera.

    Args:
        objetivo: numero entero a partir del cual buscar.

    Returns:
        El primo mas cercano a objetivo. En caso de empate, el menor
        de los dos.
    """
    objetivo = max(objetivo, 2)
    distancia = 0
    while True:
        for candidato in (objetivo - distancia, objetivo + distancia):
            if candidato >= 2 and es_primo(candidato):
                return candidato
        distancia += 1


def tiempo_medio_busqueda(
    estructura: ListaEnlazada | TablaHash, guias_a_buscar: list[int]
) -> float:
    """Mide el tiempo medio de una sola busqueda en una estructura.

    Corre REPETICIONES rondas de busquedas sobre guias_a_buscar,
    cronometrando solo las llamadas a buscar, y toma la mediana del
    tiempo total de cada ronda dividida entre el numero de guias
    buscadas.

    Args:
        estructura: ListaEnlazada o TablaHash ya construida.
        guias_a_buscar: guias a buscar en cada ronda.

    Returns:
        El tiempo medio en segundos de una sola busqueda.
    """
    tiempos_totales = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in guias_a_buscar:
            estructura.buscar(guia)
        fin = time.perf_counter()
        tiempos_totales.append(fin - inicio)
    return statistics.median(tiempos_totales) / len(guias_a_buscar)


def construir_estructuras(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una ListaEnlazada y una TablaHash con las mismas guias.

    Args:
        guias: guias a insertar en ambas estructuras, todas con el
            mismo estado ficticio "en bodega".
        m: numero de casillas de la tabla hash.

    Returns:
        Una tupla (lista, tabla) con ambas estructuras ya construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        lista.insertar(guia, "en bodega")
        tabla.insertar(guia, "en bodega")
    return lista, tabla


def verificar_coinciden(
    lista: ListaEnlazada, tabla: TablaHash, guias: list[int]
) -> None:
    """Verifica que lista y tabla devuelvan el mismo estado para guias.

    Args:
        lista: ListaEnlazada construida con las mismas guias que tabla.
        tabla: TablaHash construida con las mismas guias que lista.
        guias: guias existentes sobre las que comparar (se toma una
            muestra de hasta 50).
    """
    for guia in guias[:50]:
        assert lista.buscar(guia) == tabla.buscar(guia)


def experimento_a() -> dict[str, list[float]]:
    """Mide el tiempo de busqueda de guias inexistentes frente a n.

    Para cada n en TAMANOS_N, construye una ListaEnlazada y una
    TablaHash con m primo cercano a n / 2 (alfa ~ 2), y mide el tiempo
    medio de busqueda de BUSQUEDAS_POR_MEDICION guias inexistentes en
    cada una.

    Returns:
        Un diccionario con las listas de tiempos medios ("Lista
        enlazada" y "Tabla hash"), una entrada por n en TAMANOS_N, en
        el mismo orden.
    """
    resultados: dict[str, list[float]] = {
        "Lista enlazada": [],
        "Tabla hash": [],
    }
    for n in TAMANOS_N:
        guias = generar_guias_existentes(n)
        m = primo_cercano(max(n // 2, 1))
        lista, tabla = construir_estructuras(guias, m)
        verificar_coinciden(lista, tabla, guias)

        inexistentes = generar_guias_inexistentes(
            set(guias), BUSQUEDAS_POR_MEDICION, SEMILLA_INEXISTENTES
        )
        tiempo_lista = tiempo_medio_busqueda(lista, inexistentes)
        tiempo_tabla = tiempo_medio_busqueda(tabla, inexistentes)

        resultados["Lista enlazada"].append(tiempo_lista)
        resultados["Tabla hash"].append(tiempo_tabla)
        print(
            f"n={n:6d}  m={m:6d}  alfa={n / m:.3f}  "
            f"lista={tiempo_lista * 1e6:9.3f} us  "
            f"tabla={tiempo_tabla * 1e6:9.3f} us"
        )
    return resultados


def experimento_b() -> list[float]:
    """Mide el tiempo de busqueda de guias inexistentes frente a alfa.

    Con n = N_FIJO_EXPERIMENTO_B guias fijas, construye una TablaHash
    distinta para cada valor de ALFAS (variando m), y mide el tiempo
    medio de busqueda de BUSQUEDAS_POR_MEDICION guias inexistentes en
    cada una.

    Returns:
        La lista de tiempos medios de busqueda, una entrada por alfa
        en ALFAS, en el mismo orden.
    """
    guias = generar_guias_existentes(N_FIJO_EXPERIMENTO_B)
    inexistentes = generar_guias_inexistentes(
        set(guias), BUSQUEDAS_POR_MEDICION, SEMILLA_INEXISTENTES
    )
    tiempos: list[float] = []
    for alfa in ALFAS:
        m = max(round(N_FIJO_EXPERIMENTO_B / alfa), 1)
        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "en bodega")

        tiempo_tabla = tiempo_medio_busqueda(tabla, inexistentes)
        tiempos.append(tiempo_tabla)
        print(
            f"alfa={alfa:5.2f}  m={m:6d}  "
            f"alfa_real={tabla.factor_carga():.3f}  "
            f"tabla={tiempo_tabla * 1e6:9.3f} us"
        )
    return tiempos


def graficar_lista_vs_tabla(resultados: dict[str, list[float]]) -> None:
    """Genera graficas/lista_vs_tabla.png: tiempo medio vs. n.

    Args:
        resultados: salida de experimento_a().
    """
    plt.figure(figsize=(8, 6))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS_N, tiempos, marker="o", label=nombre)
    plt.title("Busqueda de guias inexistentes: lista vs. tabla hash")
    plt.xlabel("Numero de guias almacenadas (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def graficar_tiempo_vs_alfa(tiempos: list[float]) -> None:
    """Genera graficas/tiempo_vs_alfa.png: tiempo medio vs. factor de carga.

    Args:
        tiempos: salida de experimento_b().
    """
    plt.figure(figsize=(8, 6))
    plt.plot(ALFAS, tiempos, marker="o", label="Tabla hash")
    plt.title(
        "Tabla hash: tiempo de busqueda vs. factor de carga "
        f"(n = {N_FIJO_EXPERIMENTO_B})"
    )
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    print("Experimento A: lista vs. tabla frente a n")
    resultados_a = experimento_a()
    graficar_lista_vs_tabla(resultados_a)

    print("\nExperimento B: tabla frente a factor de carga")
    resultados_b = experimento_b()
    graficar_tiempo_vs_alfa(resultados_b)

    print(f"\nGraficas guardadas en {CARPETA_GRAFICAS}")
