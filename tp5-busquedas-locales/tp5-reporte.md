# **Informe TP N° 5**

## **Introducción: Descripción general del problema**

El problema de las N-reinas es un desafío clásico de la teoría de la computación, en el cual se busca ubicar N reinas en un tablero de ajedrez de N×N de manera que ninguna reina amenace a otra. Es decir, no deben haber dos reinas en la misma fila, columna o diagonal. Resolver este problema de forma óptima requiere encontrar configuraciones válidas para diferentes tamaños de N, lo que lo convierte en un caso interesante para probar y comparar la efectividad de algoritmos de búsqueda local, tales como Hill Climbing, Simulated Annealing y algoritmos genéticos. El objetivo principal es encontrar una solución óptima en un tiempo razonable, minimizando la cantidad de ataques entre reinas.

## **Marco teórico: Descripción teórica y general de los algoritmos puestos a prueba**

**Hill Climbing (Ascenso de colinas):** 

Este algoritmo es una técnica de búsqueda local que parte de un estado inicial y busca mejorar la solución actual mediante pequeños cambios incrementales. Se selecciona el vecino con mejor valor en función de una medida heurística. Sin embargo, es susceptible de quedar atrapado en óptimos locales, lo que puede impedir que encuentre la solución global óptima.

**Simulated Annealing (Recocido simulado):**

Es un algoritmo probabilístico que permite evitar caer en óptimos locales. Inspirado en el proceso de recocido metalúrgico, permite exploraciones más amplias del espacio de soluciones mediante la aceptación de soluciones peores en las primeras etapas del proceso, lo que reduce el riesgo de quedar atrapado en máximos locales. Conforme avanza, se disminuye gradualmente la probabilidad de aceptar peores soluciones.

**Algoritmos genéticos:**

Estos algoritmos están inspirados en los procesos de evolución biológica. Utilizan una población de soluciones (individuos) que se someten a operaciones de selección, cruzamiento y mutación para generar nuevas soluciones. La selección favorece a los individuos con mejor aptitud (menor número de ataques en el caso de las N-reinas), mientras que las mutaciones y el cruzamiento permiten la exploración de nuevas áreas del espacio de búsqueda.

## **Diseño experimental: Descripción de los experimentos**

Se implementaron los tres algoritmos descritos previamente (Hill Climbing, Simulated Annealing y algoritmos genéticos) para resolver el problema de las N-reinas en tableros de tamaño 4, 8 y 10 reinas. Cada algoritmo se ejecutó 30 veces para cada tamaño de tablero con el fin de obtener resultados consistentes y comparables.

Los experimentos se enfocaron en medir tres aspectos principales:

**Número de soluciones óptimas encontradas:** Se registró cuántas veces los algoritmos lograron encontrar una solución válida para cada tamaño de tablero.

**Tiempo de ejecución:** Se midió el tiempo promedio necesario para alcanzar una solución y su desviación estándar. Para ello, se utilizó la función time.time() de Python.

**Cantidad de estados previos explorados:** Se contabilizó el número promedio de estados que los algoritmos visitaron antes de llegar a una solución válida, así como su desviación estándar.

Además, se generaron gráficos de caja y bigotes (boxplots) que muestran la distribución de los tiempos de ejecución y la cantidad de estados explorados por cada algoritmo. También se graficó la variación de la función heurística H (cantidad de ataques entre reinas) a lo largo de las iteraciones de cada algoritmo en una ejecución específica.


## **Análisis y discusión de resultados:**

### **Gráficos:**
- **Tiempos de ejecución:**

 ![Hill Climbing:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Tiempos%20de%20ejecuci%C3%B3n%20hill%20climbing_boxplot.png) 

![Simmulated Annealing:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Tiempos%20de%20ejecuci%C3%B3n%20simmulating_boxplot.png) 

![Genetic Algorithm:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Tiempos%20alg.%20gen%C3%A9tico_boxplot.png)

- **Iteraciones:**

![Hill Climbing:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Iteraciones%20hill%20climbing_boxplot.png)

![Simmulated Annealing:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Tiempos%20de%20ejecuci%C3%B3n%20simmulating_boxplot.png)

![Genetic Algorithm:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Iteraciones%20alg.%20gen%C3%A9tico_boxplot.png)

- **Funcion H():**

La variación de la funcion H() se grafico para la iteración número 10.

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/H()%204%20reinas_boxplot.png)

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/H()%2010%20reinas_boxplot.png)

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/H()%2010%20reinas_boxplot.png)

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp5-busquedas-locales/images/Variaci%C3%B3n%20H()_boxplot.png)

Podemos observar que la función H() en Simmulated Annealing varía muchísimo más y esto es debido a que acepta entrar a estados peores.  Por otro lado, a comparación de Hill Climbing, realiza muchas más iteraciones, pero menos que el Algoritmo Genético. Y, en relación a los tiempos de ejecución, GA es quién más tiempo consume, mientras que Hill Climbing el que menos. Esto es debido a que Hill Climbing no acepta entrar a estados peores, por lo que la mayoría de las veces no encuentra la solución óptima.

## **Conclusiones:**

Podemos concluir que Simmulated Annealing es el algoritmo más eficiente en este caso, debido a que es quien encuentra el mayor porcentaje de soluciones óptimas, y además, la cantidad de iteraciones y de tiempo de ejecución es intermedio en comparación a los demás algoritmos.








