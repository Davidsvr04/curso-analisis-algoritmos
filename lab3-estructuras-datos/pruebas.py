"""Pruebas de ListaEnlazada y TablaHash."""

import random

from estructuras import ListaEnlazada, TablaHash

# Busqueda exitosa e infructuosa en la lista enlazada.
lista = ListaEnlazada()
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(1000000099) is None

# Busqueda exitosa e infructuosa en la tabla hash.
tabla = TablaHash(101)
tabla.insertar(1000000010, "en bodega")
tabla.insertar(1000000024, "en reparto")
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(1000000099) is None

# Colision forzada: con m=7, las guias 10, 24 y 17 caen en la misma
# casilla (10 % 7 = 3, 24 % 7 = 3, 17 % 7 = 3).
tabla_colision = TablaHash(7)
for guia in (10, 24, 17):
    tabla_colision.insertar(guia, "en bodega")

assert tabla_colision.hash(10) == 3
assert tabla_colision.hash(24) == 3
assert tabla_colision.hash(17) == 3
assert tabla_colision.buscar(10) == "en bodega"
assert tabla_colision.buscar(24) == "en bodega"
assert tabla_colision.buscar(17) == "en bodega"
assert tabla_colision.casillas[3].tamano == 3
assert tabla_colision.factor_carga() == 3 / 7

# Veinte colecciones aleatorias: para guias existentes e inexistentes,
# la lista y la tabla deben devolver lo mismo.
generador = random.Random(42)
estados_posibles = ["en bodega", "en reparto", "entregado"]
for _ in range(20):
    n = generador.randint(1, 100)
    guias = generador.sample(range(10**9, 10**9 + 100_000), n)
    m = generador.choice([1, 7, 11, 50, 101])

    lista_prueba = ListaEnlazada()
    tabla_prueba = TablaHash(m)
    for guia in guias:
        estado = generador.choice(estados_posibles)
        lista_prueba.insertar(guia, estado)
        tabla_prueba.insertar(guia, estado)

    for guia in guias:
        assert lista_prueba.buscar(guia) == tabla_prueba.buscar(guia)

    inexistentes = generador.sample(
        range(10**9 + 100_000, 10**9 + 200_000), 10
    )
    for guia in inexistentes:
        assert lista_prueba.buscar(guia) is None
        assert tabla_prueba.buscar(guia) is None

print("Todas las pruebas pasaron.")
