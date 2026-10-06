# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** David Viloria · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `29f379f`

Muy buen trabajo: se nota que midió, calculó y relacionó todo con el caso Tamiza.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 24 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que cumpla la ventana de cuatro horas, y nombra esa restricción.
- Explica con números por qué un servidor del doble de velocidad no basta (el tiempo crece con el cuadrado de los datos).
- Su segundo ejemplo (matrícula de materias) tiene cantidad de datos y restricción de tiempo claras.
- Identifica dos perjuicios (paciente y operador) y dice quién asume el costo, y habla de la obligación de ordenar bien porque la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- La parte ambiental dice que el consumo "es enorme", pero no lo estima ni lo conecta con horas de procesador por año. Un cálculo aproximado haría el argumento más sólido.
- El costo para la Secretaría o el equipo de desarrollo se menciona muy de pasada.

## 2. Calidad de la explicación teórica (24 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué entradas y con qué tamaño fijo, y elige el peor caso justificando por qué.
- Dejó la predicción antes de medir, razonada para cada escenario.
- La recurrencia de merge sort explica cada término, y el árbol de recursión muestra costo por nivel, número de niveles y costo total.
- El análisis línea a línea de insertion sort y la tabla de complejidades están completos.

**Lo que puede mejorar:**
- En el cálculo línea a línea, el costo de la línea `break` y de las líneas de desplazamiento queda con aproximaciones ("± O(n)"); conviene dejarlo exacto o explicar mejor por qué no cambia el resultado.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien (de mayor a menor, declarado y consistente), no cambian la lista recibida y cuentan solo comparaciones entre elementos.
- No usa `sorted()` ni `sort()`; merge sort tiene su propia mezcla recursiva.
- Los generadores dan listas del tamaño pedido, sin repetidos y con semilla.
- Cumple PEP 8, tiene tipos y docstrings en todas las funciones.

**Lo que puede mejorar:**
- Las funciones auxiliares de merge sort sí modifican la lista que reciben (es la copia interna, así que no afecta al usuario); basta aclararlo, y ya lo hace en el docstring.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados y leyenda, y los escenarios van en los mismos ejes.
- Identifica con datos exactos el peor caso (inverso, n(n-1)/2), el mejor (casi ordenado) y el promedio (aleatorio, cerca de n²/4).
- La conclusión de la Parte 4 describe qué hace cada curva y la contrasta con las complejidades; explica por qué merge sort ya gana en tamaños pequeños.
- El concepto técnico recomienda merge sort, descarta el servidor con un dato medido y estima las 10 horas de insertion sort, declarándolo como estimación.

**Lo que puede mejorar:**
- Las gráficas con tiempos muy distintos se ven pegadas al eje en tamaños pequeños; una escala logarítmica ayudaría a leer la forma de las curvas.
- Del concepto técnico faltó discutir más de una consideración distinta del tiempo apoyada en datos (solo trata la memoria).

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos siguen la estructura pedida, las gráficas se ven en el informe, hay instrucciones para reproducir y enlaces al código en cada parte.
- Hay cinco commits sobre el laboratorio con mensajes descriptivos.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores y generan las tres gráficas. Probé ambos algoritmos con listas vacías, pequeñas, aleatorias y repetidas, y ordenan bien.

## Para el próximo laboratorio
- Estime números concretos en la parte ambiental (por ejemplo, horas de procesador por año).
- Use escala logarítmica o una gráfica adicional para ver mejor tamaños pequeños.
- Deje exactas las cuentas línea a línea, incluyendo el `break`.
- Discuta más de una consideración adicional (memoria, estabilidad, mantenimiento) con datos propios.
