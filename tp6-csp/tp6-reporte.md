# **Trabajo Práctico 6: Satisfacción de restricciones**

 ### **1. Describir en detalle una formulación CSP para el Sudoku.**

 El Sudoku es un rompecabezas en el que se tiene una cuadrícula de 9×9 con algunas celdas pre-rellenadas con números entre 1 y 9. El objetivo es llenar las celdas vacías de modo que:

- Cada fila contenga los números del 1 al 9 sin repetirse.
- Cada columna contenga los números del 1 al 9 sin repetirse.
- Cada subcuadro de 3×3 contenga los números del 1 al 9 sin repetirse.
  
**Elementos del CSP:**

1. **Variables:** Cada celda en la cuadrícula 9×9 se considera una variable. Por lo tanto, el conjunto de variables es:

    X = {X11​, X12​, ..., X99​ }
donde Xij​ representa la celda en la fila i y la columna j.

1. **Dominios:** Para cada variable Xij, el dominio es el conjunto de números posibles que pueden asignarse a esa celda. Si la celda ya está rellenada con un número (debido a las pistas iniciales), el dominio es ese número único; si está vacía, el dominio es {1, 2, ..., 9}.

2. **Restricciones:**

    **Restricciones unarias:** Estas restricciones se aplican a variables individuales. Para el Sudoku, las restricciones unarias se aplican a las celdas que ya tienen un valor fijo (por ejemplo, X11 = 5).

    **Restricciones binarias:** Estas restricciones se aplican entre pares de variables. En Sudoku, las restricciones binarias aseguran que las variables de la misma fila, columna o subcuadro de 3×3 no tomen el mismo valor. Por ejemplo:

    X11 ≠ X12, X11 ≠ X21, X11 ≠ X22, ...

    **Restricciones de nivel superior:** Aunque se puede formular el Sudoku solo con restricciones binarias, se puede expresar con restricciones más generales, como que un conjunto de 9 variables (una fila, columna o subcuadro) debe tomar valores diferentes en el rango {1, 2, ..., 9}. Esta formulación reduce la complejidad en la expresión de las restricciones.

### **2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial WA=red, V=blue para el problema de colorear el mapa de Australia (Figura 6.1 AIMA 3ra edición).**

Seguimos el procedimiento de AC-3 iterando sobre los arcos en un orden posible, eliminando valores inconsistentes de los dominios. A continuación, trazaremos cada iteración de un bucle while en el algoritmo AC-3 para una posible ordenación de los arcos:

### Paso a paso del Algoritmo AC-3:

1. **Q = {SA - WA, SA - V, NT - WA, NT - SA, NSW - SA, NSW - V, Q - NT, Q - SA, Q - NSW}**

   - **Asignación parcial**: \{WA = verde, V = rojo\}

### Iteraciones del Bucle while en AC-3:

1. **Eliminar SA - WA**:
   - WA ya está asignado a verde, por lo que debemos eliminar el valor verde del dominio de SA.
   - **Dominio de SA**: \{rojo, azul\} 
   - Como el dominio de SA ha cambiado, los arcos que involucran a SA deben volver a añadirse a la cola, es decir, añadimos los arcos que dependen de SA (SA - V, NT - SA, NSW - SA, Q - SA).

2. **Eliminar SA - V**:
   - V ya está asignado a rojo, por lo que debemos eliminar el valor rojo del dominio de SA.
   - **Dominio de SA** antes: \{rojo, azul\}.
   - **Dominio de SA** después: \{azul\} (se elimina rojo).
   - Como el dominio de SA ha cambiado, volvemos a añadir los arcos relacionados con SA.

3. **Eliminar NT - WA**:
   - WA ya está asignado a verde, por lo que debemos eliminar el valor verde del dominio de NT.
   - **Dominio de NT** antes: \{rojo, azul, verde\}.
   - **Dominio de NT** después: \{rojo, azul\} (se elimina verde).
   - Como el dominio de NT ha cambiado, los arcos que dependen de NT (NT - SA, Q - NT) deben volver a añadirse a la cola.

4. **Eliminar NT - SA**:
   - En este punto, SA solo tiene el valor azul en su dominio, por lo que debemos eliminar el valor azul del dominio de NT, ya que no pueden tomar el mismo valor.
   - **Dominio de NT** antes: \{rojo, azul\}.
   - **Dominio de NT** después: \{rojo\} (se elimina azul).
   - Como el dominio de NT ha cambiado, los arcos que dependen de NT deben volver a añadirse a la cola.

5. **Eliminar NSW - SA**:
   - SA tiene asignado azul como único valor en su dominio, por lo que NSW no puede tener el valor azul.
   - **Dominio de NSW** antes: \{rojo, azul, verde\}.
   - **Dominio de NSW** después: \{rojo, verde\} (se elimina azul).
   - Como el dominio de NSW ha cambiado, volvemos a añadir los arcos relacionados con NSW.

6. **Eliminar NSW - V**:
   - V ya está asignado a rojo, por lo que debemos eliminar el valor rojo del dominio de NSW.
   - **Dominio de NSW** antes: \{rojo, verde\}.
   - **Dominio de NSW** después: \{verde\} (se elimina rojo).
   - Como el dominio de NSW ha cambiado, los arcos relacionados con NSW deben ser añadidos de nuevo.

7. **Eliminar Q - NT**:
   - NT tiene asignado rojo como único valor en su dominio, por lo que debemos eliminar rojo del dominio de Q.
   - **Dominio de Q** antes: \{rojo, azul, verde\}.
   - **Dominio de Q** después: \{azul, verde\} (se elimina rojo).
   - Como el dominio de Q ha cambiado, añadimos de nuevo los arcos que dependen de Q.

8. **Eliminar Q - SA**:
   - SA tiene asignado azul como único valor en su dominio, por lo que debemos eliminar el valor azul del dominio de Q.
   - **Dominio de Q** antes: \{azul, verde\}.
   - **Dominio de Q** después: \{verde\} (se elimina azul).
   - Como el dominio de Q ha cambiado, volvemos a añadir los arcos relacionados con Q.

9. **Eliminar Q - NSW**:
   - NSW tiene asignado verde como único valor en su dominio, por lo que debemos eliminar verde del dominio de Q.
   - **Dominio de Q** antes: \{verde\}.
   - **Dominio de Q** después: vacío (se elimina verde).
   - **Dominio de Q**: vacío. Esto indica que no hay valores posibles para \( Q \), lo que implica una inconsistencia.

### Conclusión:

El algoritmo AC-3 detectó una inconsistencia porque el dominio de Q quedó vacío. Esto significa que la asignación parcial \{WA = verde, V = rojo\} es inconsistente con las restricciones del problema, y no hay forma de asignar un valor válido a todas las variables.

### **3. ¿Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP? (i.e. cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).**

En el caso de un CSP estructurado como un árbol:

- E es el número de arcos (o restricciones) en el grafo.
- D es el tamaño del dominio más grande de las variables.

Por lo tanto, la complejidad en el peor caso de AC-3 en un CSP con estructura de árbol es O(ED)

Esto se debe a que cada arco es revisado como máximo una vez, y para cada arco, la verificación de consistencia entre los valores de los dominios de las variables involucradas toma (O(D)) tiempo.

### **4. AC-3 coloca de nuevo en la cola todo arco (Xk,Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk,Xi) se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk. Explicar cómo actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2.d^2).**

La idea básica es preprocesar las restricciones de manera que, para cada valor de Xi, llevemos un registro de aquellas variables Xk para las cuales un arco de Xk a Xi es satisfecho por ese valor particular de Xi. Esta estructura de datos puede calcularse en un tiempo proporcional al tamaño de la representación del problema. Luego, cuando se elimina un valor de Xi, reducimos en 1 el conteo de valores permitidos para cada arco (Xk, Xi) registrado bajo ese valor.

### Descripción del proceso:

1. **Preprocesamiento de restricciones**: 
   - Para cada valor de una variable X_i, mantenemos un registro de las variables X_k cuyos arcos hacia X_i son consistentes con ese valor particular de X_i.
   - Este preprocesamiento permite que, cuando eliminemos un valor de X_i, sepamos qué arcos se ven afectados.

2. **Actualización eficiente**:
   - Cada vez que se elimina un valor del dominio de X_i, reducimos en 1 el conteo de los valores permitidos para cada variable X_k que depende de X_i, usando la estructura de datos previamente calculada.
   - Al mantener este registro, evitamos la necesidad de volver a verificar cada arco desde cero, lo que hace que la actualización sea más eficiente.

### Complejidad total \(O(n^2d^2)\):

- n es el número de variables y d es el tamaño del dominio más grande.
- Para cada par de variables, hay a lo sumo d^2 pares de valores a verificar, ya que para cada valor de X_i, tenemos que asegurarnos de que haya un valor en X_k que sea consistente.
- Este enfoque asegura que el algoritmo de consistencia de arcos se ejecute en tiempo total O(n^2d^2), ya que el preprocesamiento y las actualizaciones se realizan de manera eficiente en términos del número de arcos y valores posibles.

Este enfoque optimiza la verificación de consistencia de arcos al reducir la cantidad de verificaciones necesarias después de eliminar valores, al mantener actualizados los conteos de valores consistentes entre las variables relacionadas.

### ** 5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 6.5, AIMA 3da edición). Para ello, demostrar:
a. Para un CSP cuyo grafo de restricciones es un árbol, la 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)

b. Argumentar por qué lo demostrado en 5a es suficiente.

**Demostración:**

Supongamos que tenemos un CSP cuyo grafo de restricciones es un árbol y hemos logrado la 2-consistencia. Esto significa que para cada par de variables (Xi, Xj) en el CSP, cualquier valor en el dominio de Xi es consistente con al menos un valor en el dominio de Xj, y viceversa.

Para demostrar la n-consistencia, consideremos cualquier variable Xi en el CSP. Dado que el grafo de restricciones es un árbol, Xi está relacionada con el resto de las variables a través de un único camino en el árbol. Denotemos las variables en este camino como X1, X2, ..., Xn, donde X1 = Xi.

Dado que hemos logrado la 2-consistencia, sabemos que para cualquier variable Xk en el camino (donde k > 1), hay al menos un valor en el dominio de Xk que es consistente con algún valor en el dominio de Xk-1. Esto es cierto para todas las variables en el camino.

Por lo tanto, hemos demostrado que para cualquier variable Xi en el CSP, cualquier valor en su dominio es consistente con al menos un valor en el dominio de cada otra variable en el CSP, siguiendo el único camino en el árbol de restricciones.

Este resultado es suficiente porque, en un CSP, el objetivo es encontrar una asignación que cumpla con todas las restricciones. Si hemos logrado que todas las variables sean consistentes entre sí, hemos eliminado cualquier conflicto y hemos asegurado que existe una solución que satisface todas las restricciones. Esto es fundamental para la correctitud del algoritmo CSP en árboles estructurados, ya que garantiza que si una solución existe, el algoritmo la encontrará.


### **Resultados obtenidos tras la ejecución de los algoritmos:**

4 reinas

- **Algoritmo: Forward checking**
- Porcentaje de soluciones óptimas: 1.00
- Tiempo de ejecución promedio: 0.0000 segundos
- Iteraciones: 9.00
- Desviación estándar del tiempo de ejecución: 0.0000 segundos
- **Algoritmo: Backtraking**
- Porcentaje de soluciones óptimas: 1.00
- Tiempo de ejecución promedio: 0.0000 segundos
- Iteraciones: 9.00
- Desviación estándar del tiempo de ejecución: 0.0000 segundos

8 reinas

- **Algoritmo: Forward checking**
- Porcentaje de soluciones óptimas: 1.00
- Tiempo de ejecución promedio: 0.0001 segundos
- Iteraciones: 114.00
- Desviación estándar del tiempo de ejecución: 0.0004 segundos
- **Algoritmo: Backtraking**
- Porcentaje de soluciones óptimas: 1.00
- Tiempo de ejecución promedio: 0.0025 segundos
- Iteraciones promedio: 79.00
- Desviación estándar del tiempo de ejecución: 0.0053 segundos

10 reinas
- **Algoritmo: Forward checking**
- Porcentaje de soluciones óptimas: 1.00
- Tiempo de ejecución promedio: 0.0003 segundos
- Iteraciones: 103.00
- Desviación estándar del tiempo de ejecución: 0.0006 segundos
- **Algoritmo: Backtraking**
- Porcentaje de soluciones óptimas: 1.00
- Tiempo de ejecución promedio: 0.0111 segundos
- Iteraciones: 281.00
- Desviación estándar del tiempo de ejecución: 0.0077 segundos

### **Gráficos de caja y bigotes:**

![Tiempos BACKTRACKING](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp6-csp/images/Tiempos%20de%20ejecuci%C3%B3n%20BACKTRACKING_boxplot.png)

![Tiempos FORWARD CHECKING](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp6-csp/images/Tiempos%20de%20ejecuci%C3%B3n%20FORWARD%20CHECKING_boxplot.png)

![Tiempos HILL CLIMBING](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp6-csp/images/Tiempos%20de%20ejecuci%C3%B3n%20hill%20climbing_boxplot.png)

![Tiempos SIMMULATED ANNEALING](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp6-csp/images/Tiempos%20de%20ejecuci%C3%B3n%20simmulating_boxplot.png)

![Tiempos GENETIC](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp6-csp/images/Tiempos%20alg.%20gen%C3%A9tico_boxplot.png)

Podemos ver que los tiempos de ejecución de Forward Checking son menores a los de Backtracking, y este ultimo tiene tiempos de ejecución similares a los algoritmos de Simmulated Annealing y Hill Climbing, mientras que el algortitmo Genético sigue siendo el que más tiempo toma.