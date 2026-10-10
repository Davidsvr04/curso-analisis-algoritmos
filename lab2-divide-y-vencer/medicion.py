"""Experimento de medicion: fuerza bruta vs. divide y venceras.

Mide el tiempo de ejecucion de subarreglo_fuerza_bruta y
subarreglo_maximo sobre la misma lista de variacion diaria de caja,
para varios tamanos de entrada, y grafica ambas curvas en los mismos
ejes.
"""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_valores(n: int, semilla: int = SEMILLA) -> list[float]:
    """Genera n variaciones diarias de caja, enteras entre -100 y 100.

    Args:
        n: cantidad de dias (tamano de la lista).
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n valores (como float) entre -100 y 100, inclusive.
    """
    generador = random.Random(semilla)
    return [float(generador.randint(-100, 100)) for _ in range(n)]


def medir_tiempo(
    funcion, *args
) -> tuple[float, tuple[int, int, float]]:
    """Mide el tiempo mediano de REPETICIONES llamadas a funcion(*args).

    Cronometra unicamente la llamada a funcion con
    time.perf_counter(), nunca la generacion de los datos.

    Args:
        funcion: subarreglo_fuerza_bruta o subarreglo_maximo.
        *args: argumentos posicionales para funcion.

    Returns:
        Una tupla con el tiempo mediano en segundos de las
        REPETICIONES corridas y el resultado (inicio, fin, suma)
        devuelto por la ultima corrida.
    """
    tiempos = []
    resultado = None
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado = funcion(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return statistics.median(tiempos), resultado


def ejecutar_experimento() -> dict[str, list[float]]:
    """Corre ambos algoritmos sobre los mismos datos, para todos los tamanos.

    Verifica, en cada tamano, que ambos algoritmos devuelven la misma
    suma maxima.

    Returns:
        Un diccionario indexado por nombre de algoritmo ("Fuerza
        bruta" y "Divide y venceras"), con la lista de tiempos
        medianos (uno por tamano en TAMANOS, en el mismo orden).
    """
    resultados: dict[str, list[float]] = {
        "Fuerza bruta": [],
        "Divide y venceras": [],
    }
    for n in TAMANOS:
        valores = generar_valores(n)

        tiempo_bf, resultado_bf = medir_tiempo(
            subarreglo_fuerza_bruta, valores
        )
        tiempo_dv, resultado_dv = medir_tiempo(
            subarreglo_maximo, valores, 0, n - 1
        )
        suma_bf = resultado_bf[2]
        suma_dv = resultado_dv[2]

        assert suma_bf == suma_dv, (
            f"n={n}: fuerza bruta dio {suma_bf}, "
            f"divide y venceras dio {suma_dv}"
        )

        resultados["Fuerza bruta"].append(tiempo_bf)
        resultados["Divide y venceras"].append(tiempo_dv)
        print(
            f"n={n:6d}  fuerza_bruta={tiempo_bf:.6f}s  "
            f"divide_y_venceras={tiempo_dv:.6f}s  suma_max={suma_bf}"
        )
    return resultados


def graficar_tiempo(resultados: dict[str, list[float]]) -> None:
    """Genera graficas/tiempo_vs_n.png: tiempo vs. tamano de entrada.

    Args:
        resultados: salida de ejecutar_experimento().
    """
    plt.figure(figsize=(8, 6))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)
    plt.title("Subarreglo maximo: fuerza bruta vs. divide y venceras")
    plt.xlabel("Tamano de entrada n (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_n.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    resultados = ejecutar_experimento()
    graficar_tiempo(resultados)
    print(f"\nGrafica guardada en {CARPETA_GRAFICAS}")
