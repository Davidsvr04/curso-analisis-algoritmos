# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** David Viloria · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `3e226a7`

Excelente trabajo: un informe muy completo, con datos propios y razonamientos claros.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **98 / 100** |
| **Nota (0–5)** | **4.90** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identificó con sus datos dónde divide y vencerás empieza a ganar (desde n=50) y explicó por qué en n=10 pierde.
- Comparó con el máximo de un arreglo: mostró que combinar cuesta poco, la recurrencia da `Θ(n)` y dividir solo añade trabajo extra.
- Recomendó divide y vencerás y estimó el tiempo a 1.000.000 de registros (unas 6 horas contra unos 2 segundos), declarándolo como estimación y sin regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 3, el cruce en n=10 se explica con "ruido" y "costo fijo" sin respaldarlo con una medición; con más repeticiones en tamaños pequeños sería más sólido.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- La recurrencia `T(n) = 2T(n/2) + Θ(n)` está bien explicada término por término.
- Aplicó el método maestro verificando la condición del caso 2.
- Justificó el `Θ(n²)` de la fuerza bruta con la suma n + (n−1) + ... + 1.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta y ninguna función modifica la lista recibida.
- Las pruebas cubren todos los casos pedidos y verifican que la lista no se modifica.

**Lo que puede mejorar:**
- En `medicion.py`, la función `medir_tiempo` no tiene tipo indicado para su parámetro `funcion`.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calculó el factor al duplicar n (×4,07 para fuerza bruta y ×1,85 para divide y vencerás) y lo contrastó con `Θ(n²)` y `Θ(n log n)`.
- Las cifras del informe coinciden con la gráfica publicada (cerca de 0,35 s en n=4000 y 1,43 s en n=8000 para fuerza bruta).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas pedida, el orden del informe, los enlaces al código y la gráfica incrustada con ruta que funciona.
- Incluyó instrucciones de reproducción y cuatro commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos dan las mismas sumas en listas aleatorias y el experimento corre y genera la gráfica sin problemas.

## Para el próximo laboratorio
- Indique el tipo de todos los parámetros de las funciones, incluidos los que reciben otras funciones.
- Deje dos líneas en blanco entre funciones y *docstrings* con `Args` y `Returns` en todas.
- Repita más veces las mediciones de tamaños muy pequeños y apoye sus explicaciones en esos datos.
