# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** David Viloria · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-02 23:59 · **Versión revisada:** commit `74653d7`

Muy buen trabajo: el laboratorio está completo, ordenado y con un análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **98 / 100** |
| **Nota (0–5)** | **4.90** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque sobren casillas, y usa el ejemplo de las guías 10, 24 y 17 con `m = 7`.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica que la tabla no sirve para rangos y que el árbol sí, y estima la altura del árbol degenerado frente al equilibrado.
- Recomienda una combinación (tabla hash más árbol equilibrado) y declara que la cifra para 5.000.000 de envíos es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- Para el árbol degenerado da la altura y las comparaciones de una búsqueda, pero no el total de comparaciones al insertar las 400.000 guías una a una.
  → *Cómo corregirlo:* piense cuántos nodos recorre la guía número 1, la número 2, la número 3, y sume esa secuencia hasta 400.000; haga lo mismo con el árbol equilibrado y compare los dos totales.
- La estimación de la tabla a 5.000.000 se queda en "menos de 1 µs" sin conectarla con su propia gráfica.
  → *Cómo corregirlo:* apóyese en los valores medidos de la tabla con α fijo y diga qué pasaría con α si `m` no creciera junto con `n`, usando la segunda gráfica.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica por qué la búsqueda de una guía inexistente en la lista recorre los `n` nodos, y de dónde sale el `Θ(1 + α)` de la tabla (el 1 del cálculo del hash y el α de recorrer la cadena).
- Nombra el supuesto de hash uniforme simple y explica que, si todas las guías caen en una casilla, la tabla se vuelve una lista y cuesta `Θ(n)`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` inserta al inicio en tiempo constante y busca con un ciclo `while`; `TablaHash` reutiliza la lista en cada casilla, sin `dict`, `set` ni `hash()` de Python.
- `pruebas.py` cubre búsqueda exitosa e infructuosa, la colisión forzada con `m = 7` (casilla 3 con tres guías), `factor_carga() == 3 / 7` y veinte colecciones aleatorias.
- Todas las funciones tienen *docstring* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de `n` con las dos curvas en los mismos ejes y la segunda cuatro valores de α.
- Calcula factores de crecimiento de la lista entre dos valores consecutivos de `n` y los compara con `Θ(n)`.
- Lo que dice coincide con lo que se ve: en `lista_vs_tabla.png` la lista llega a unos 0,0044 s con n = 50000 y la tabla queda pegada al cero; en `tiempo_vs_alfa.png` el tiempo sube de forma continua con α.

**Lo que puede mejorar (y cómo corregirlo):**
- Para la tabla no calcula el factor de crecimiento entre dos valores consecutivos de `n`; solo dice que "no hay tendencia".
  → *Cómo corregirlo:* tome dos valores de `n` de su tabla de resultados, divida los tiempos de la tabla hash y compare con el factor por el que se multiplicó `n`.
- En la segunda gráfica dice que el crecimiento es "coherente en dirección" con `Θ(1 + α)`, pero no calcula cuánto crece el tiempo cuando α se multiplica.
  → *Cómo corregirlo:* compare dos valores de α (por ejemplo, el menor y el mayor), calcule por cuánto se multiplicó cada uno y diga si el tiempo creció en proporción parecida.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab3-estructuras-datos/` está en la ubicación acordada y tiene exactamente los archivos pedidos, incluidas las dos gráficas.
- El `README.md` sigue el orden pedido, trae su nombre, las instrucciones para reproducir, los enlaces a `estructuras.py`, `pruebas.py` y `medicion.py`, y las gráficas incrustadas con rutas relativas que funcionan.
- El laboratorio tiene cuatro commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre sin errores y genera las dos gráficas. La lista y la tabla devuelven lo mismo en todos los casos probados.
