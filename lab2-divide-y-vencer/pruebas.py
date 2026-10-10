"""Pruebas de subarreglo_fuerza_bruta, suma_cruzada y subarreglo_maximo."""

import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)

# Serie de ocho dias de la situacion problema: mejor racha del dia 2 al 7,
# suma 17.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

# Un solo elemento: el unico tramo posible es ese elemento.
assert subarreglo_fuerza_bruta([42.0])[2] == 42.0
assert subarreglo_maximo([42.0], 0, 0)[2] == 42.0
assert subarreglo_fuerza_bruta([-7.0])[2] == -7.0
assert subarreglo_maximo([-7.0], 0, 0)[2] == -7.0

# Todos los valores negativos: la mejor racha es el menos negativo de
# todos, tomado solo.
todos_negativos = [-5, -2, -8, -1, -9]
assert subarreglo_fuerza_bruta(todos_negativos)[2] == -1
assert subarreglo_maximo(todos_negativos, 0, len(todos_negativos) - 1)[2] == -1

# Todos los valores positivos: la mejor racha es la suma total.
todos_positivos = [3, 1, 4, 1, 5, 9, 2, 6]
assert subarreglo_fuerza_bruta(todos_positivos)[2] == sum(todos_positivos)
assert (
    subarreglo_maximo(todos_positivos, 0, len(todos_positivos) - 1)[2]
    == sum(todos_positivos)
)

# Caso donde el mejor tramo cruza el punto medio: con 10 elementos (indices
# 0..9), el punto medio de la primera llamada es 4. El mejor tramo real es
# valores[2..7] = [4, 5, -1, -1, 6, 7], suma 20, que cruza ese punto medio.
cruzado = [-1, -1, 4, 5, -1, -1, 6, 7, -1, -1]
assert subarreglo_fuerza_bruta(cruzado)[2] == 20
assert subarreglo_maximo(cruzado, 0, len(cruzado) - 1)[2] == 20
assert suma_cruzada(cruzado, 0, 4, len(cruzado) - 1)[2] == 20

# Veinte listas aleatorias: ambas funciones deben dar la misma suma, y
# ninguna debe modificar la lista recibida.
generador = random.Random(42)
for _ in range(20):
    n = generador.randint(1, 200)
    valores = [generador.randint(-100, 100) for _ in range(n)]
    original = list(valores)

    suma_bf = subarreglo_fuerza_bruta(valores)[2]
    suma_dv = subarreglo_maximo(valores, 0, len(valores) - 1)[2]

    assert suma_bf == suma_dv, (
        f"n={n}: fuerza bruta {suma_bf} != divide y venceras {suma_dv}"
    )
    assert valores == original

print("Todas las pruebas pasaron.")
