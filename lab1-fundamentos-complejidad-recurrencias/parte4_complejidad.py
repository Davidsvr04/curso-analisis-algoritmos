"""Experimento de la Parte 4: validacion experimental de la complejidad.

Mide el tiempo de ejecucion de insertion_sort y merge_sort sobre el
escenario A (aleatorio) de Tamiza, para los mismos tamanos de entrada
de la Parte 3, y grafica ambas curvas en los mismos ejes.
"""

import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

ALGORITMOS = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


def medir_tiempo(funcion_ordenamiento, datos: list[int]) -> float:
    """Mide el tiempo mediano de una funcion de ordenamiento instrumentada.

    Corre funcion_ordenamiento varias veces sobre la misma entrada (que
    no se modifica entre corridas, porque ninguno de los dos algoritmos
    altera la lista recibida) y toma la mediana para reducir el ruido
    de la maquina.

    Args:
        funcion_ordenamiento: insertion_sort o merge_sort.
        datos: lista de indices de riesgo a ordenar.

    Returns:
        El tiempo mediano en segundos de las REPETICIONES corridas.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        funcion_ordenamiento(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return statistics.median(tiempos)


def ejecutar_experimento() -> dict[str, list[float]]:
    """Corre ambos algoritmos sobre el escenario A, para todos los tamanos.

    Returns:
        Un diccionario indexado por nombre de algoritmo, con la lista
        de tiempos medianos (uno por tamano en TAMANOS, en el mismo
        orden).
    """
    resultados: dict[str, list[float]] = {nombre: [] for nombre in ALGORITMOS}
    for n in TAMANOS:
        datos = generar_aleatorio(n)
        for nombre, funcion in ALGORITMOS.items():
            tiempo_mediano = medir_tiempo(funcion, datos)
            resultados[nombre].append(tiempo_mediano)
            print(f"{nombre:15s} n={n:6d}  tiempo={tiempo_mediano:.6f}s")
    return resultados


def graficar_tiempo(resultados: dict[str, list[float]]) -> None:
    """Genera graficas/parte4_tiempo.png: tiempo vs. tamano, ambos algoritmos.

    Args:
        resultados: salida de ejecutar_experimento().
    """
    plt.figure(figsize=(8, 6))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)
    plt.title(
        "Insertion sort vs. merge sort: tiempo de ejecucion (escenario A)"
    )
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte4_tiempo.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = ejecutar_experimento()
    graficar_tiempo(resultados)
    print(f"\nGrafica guardada en {CARPETA_GRAFICAS}")
