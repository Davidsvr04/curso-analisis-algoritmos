"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Simula el cargue directo desde el portal web de los laboratorios:
    los registros quedan en el orden en que cada laboratorio los subio,
    sin ninguna relacion con el indice de riesgo.

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    generador = random.Random(semilla)
    datos = list(range(1, n + 1))
    generador.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Simula el reproceso sobre la lista del dia anterior: el 98% del
    lote ya quedo ordenado por riesgo (de mayor a menor, el orden que
    Tamiza necesita) y el 2% restante son los resultados nuevos del
    dia, anexados al final sin ordenar.

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    generador = random.Random(semilla)
    corte = int(n * 0.98)
    restantes = n - corte
    # Prefijo: los "corte" indices mas altos, ya en orden descendente
    # (construidos directamente en ese orden, sin usar ningun ordenamiento).
    prefijo_ordenado = list(range(n, n - corte, -1))
    # Sufijo: los indices restantes (los mas bajos), mezclados al azar.
    sufijo_desordenado = list(range(restantes, 0, -1))
    generador.shuffle(sufijo_desordenado)
    return prefijo_ordenado + sufijo_desordenado


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Simula la migracion desde el sistema legado de historia clinica,
    que exporta los registros del indice de riesgo menor al mayor: es
    decir, en orden ascendente, exactamente al reves del orden
    descendente que Tamiza necesita.

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(1, n + 1))
