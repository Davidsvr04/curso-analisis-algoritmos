"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de mayor a menor (indice de riesgo mas alto primero), que es
    el orden que necesita la plataforma Tamiza para generar la lista de
    llamadas del dia.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = 0
    for i in range(1, len(resultado)):
        clave = resultado[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if resultado[j] >= clave:
                break
            resultado[j + 1] = resultado[j]
            j -= 1
        resultado[j + 1] = clave
    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de mayor a menor (indice de riesgo mas alto primero), el
    mismo criterio usado en insertion_sort, para que ambos algoritmos
    sean comparables sobre los mismos escenarios.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = _mezclar_ordenar(resultado, 0, len(resultado) - 1)
    return resultado, comparaciones


def _mezclar_ordenar(datos: list[int], izquierda: int, derecha: int) -> int:
    """Divide y ordena recursivamente el tramo [izquierda, derecha] de datos.

    Args:
        datos: lista sobre la que se ordena en el sitio (se modifica).
        izquierda: indice inicial del tramo a ordenar, inclusive.
        derecha: indice final del tramo a ordenar, inclusive.

    Returns:
        El numero de comparaciones entre elementos realizadas al
        ordenar ese tramo.
    """
    if izquierda >= derecha:
        return 0
    medio = (izquierda + derecha) // 2
    comparaciones = _mezclar_ordenar(datos, izquierda, medio)
    comparaciones += _mezclar_ordenar(datos, medio + 1, derecha)
    comparaciones += _combinar(datos, izquierda, medio, derecha)
    return comparaciones


def _combinar(
    datos: list[int], izquierda: int, medio: int, derecha: int
) -> int:
    """Combina dos mitades ya ordenadas de datos[izquierda..derecha].

    Las mitades son datos[izquierda..medio] y datos[medio+1..derecha],
    ambas ya ordenadas de mayor a menor. Al terminar, datos[izquierda..
    derecha] queda ordenado de mayor a menor.

    Args:
        datos: lista sobre la que se combina en el sitio (se modifica).
        izquierda: indice inicial del tramo, inclusive.
        medio: indice final de la primera mitad, inclusive.
        derecha: indice final del tramo, inclusive.

    Returns:
        El numero de comparaciones entre elementos realizadas durante
        la combinacion.
    """
    mitad_izquierda = datos[izquierda:medio + 1]
    mitad_derecha = datos[medio + 1:derecha + 1]
    i = 0
    j = 0
    k = izquierda
    comparaciones = 0
    while i < len(mitad_izquierda) and j < len(mitad_derecha):
        comparaciones += 1
        if mitad_izquierda[i] >= mitad_derecha[j]:
            datos[k] = mitad_izquierda[i]
            i += 1
        else:
            datos[k] = mitad_derecha[j]
            j += 1
        k += 1
    while i < len(mitad_izquierda):
        datos[k] = mitad_izquierda[i]
        i += 1
        k += 1
    while j < len(mitad_derecha):
        datos[k] = mitad_derecha[j]
        j += 1
        k += 1
    return comparaciones
