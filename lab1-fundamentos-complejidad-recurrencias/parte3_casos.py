"""Experimento de la Parte 3: peor caso, mejor caso y caso promedio.

Ejecuta insertion_sort sobre los tres escenarios de entrada de Tamiza
(aleatorio, casi ordenado e inverso), para varios tamanos de entrada,
y grafica comparaciones y tiempo de ejecucion en funcion del tamano.
"""

import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": generar_inverso,
}


def medir_insertion_sort(datos: list[int]) -> tuple[float, int]:
    """Mide el tiempo mediano y las comparaciones de insertion_sort.

    Corre insertion_sort varias veces sobre la misma entrada (que no
    se modifica entre corridas) y toma la mediana del tiempo para
    reducir el ruido de la maquina. El numero de comparaciones es
    determinista para una misma entrada, asi que se toma de cualquier
    corrida.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con el tiempo mediano en segundos y el numero de
        comparaciones realizadas.
    """
    tiempos = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return statistics.median(tiempos), comparaciones


def ejecutar_experimento() -> dict[str, dict[str, list[float]]]:
    """Corre insertion_sort sobre los tres escenarios y todos los tamanos.

    Returns:
        Un diccionario indexado por nombre de escenario, cada uno con
        las listas paralelas "tiempo" y "comparaciones" (una entrada
        por tamano en TAMANOS, en el mismo orden).
    """
    resultados: dict[str, dict[str, list[float]]] = {
        nombre: {"tiempo": [], "comparaciones": []} for nombre in ESCENARIOS
    }
    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            datos = generador(n)
            tiempo_mediano, comparaciones = medir_insertion_sort(datos)
            resultados[nombre]["tiempo"].append(tiempo_mediano)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(
                f"{nombre:20s} n={n:6d}  "
                f"tiempo={tiempo_mediano:.6f}s  comparaciones={comparaciones}"
            )
    return resultados


def graficar_comparaciones(
    resultados: dict[str, dict[str, list[float]]]
) -> None:
    """Genera graficas/parte3_comparaciones.png: comparaciones vs. tamano.

    Args:
        resultados: salida de ejecutar_experimento().
    """
    plt.figure(figsize=(8, 6))
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte3_comparaciones.png", dpi=150)
    plt.close()


def graficar_tiempo(resultados: dict[str, dict[str, list[float]]]) -> None:
    """Genera graficas/parte3_tiempo.png: tiempo de ejecucion vs. tamano.

    Args:
        resultados: salida de ejecutar_experimento().
    """
    plt.figure(figsize=(8, 6))
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["tiempo"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "parte3_tiempo.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = ejecutar_experimento()
    graficar_comparaciones(resultados)
    graficar_tiempo(resultados)
    print(f"\nGraficas guardadas en {CARPETA_GRAFICAS}")
