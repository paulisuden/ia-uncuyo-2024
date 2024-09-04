# INFORME 
## TRABAJO PRÁCTICO N° 3 Y 4

### Introducción

 Se deben crear 30 entornos deterministas, aleatorios, de 100 × 100, cuyas celdas representen un obstáculo para el agente (agujeros en el hielo) con probabilidad 0,08. Para esto, se debe utilizar el entorno de FrozenLake y modificar la vida del agente a 1000 acciones. Por otro lado, el agente a implementar es uno basado en objetivos que, dado un punto de inicio y un punto destino, encuentre el camino óptimo (si es posible). Se deben considerar los siguientes escenarios posibles:

 Escenario 1: Cada acción tiene costo 1.

 Escenario 2: Las acciones tienen como costo asociado un entero más que el que representa a la acción, es decir, moverse a la izquierda tiene costo 1, moverse hacia abajo tiene costo 2, etc.

 El agente deberá ser capaz de resolver el problema planteado mediante los siguientes algoritmos de búsqueda no informada:

-Búsqueda por Anchura.

-Búsqueda por Profundidad.

-Búsqueda por Profundidad Limitada (l´ımite = 10).

-Búsqueda de Costo Uniforme

### Marco teórico

**FrozenLake** es un entorno de juego en el que el agente (que puede ser un robot, un personaje, etc.) debe navegar a través de un lago congelado para alcanzar un objetivo sin caer en agujeros de hielo. El entorno está representado por una cuadrícula en la que cada celda puede ser uno de los siguientes tipos:

-**S (Start)**: La celda inicial donde comienza el agente.

-**F (Frozen)**: Celda de hielo congelado por la que el agente puede moverse.

-**H (Hole)**: Celda con un agujero, que provoca que el agente caiga y pierda el juego si se mueve a ella.

-**G (Goal)**: Celda objetivo que el agente debe alcanzar para ganar el juego.

**Principales Elementos:**

1. Matriz del Entorno

2. Agente

3. Acciones

4. Estado (posición actual)

5. **is_slippery**: Un parámetro que determina si el entorno es resbaladizo. Si es True, las acciones del agente pueden no tener el efecto esperado debido a deslizamientos. Si es False, el agente se mueve exactamente en la dirección indicada.

Por otro lado, el **agente basado en objetivos**, incorpora modelos “abiertos” para:
- Objetivos a alcanzar
- Acciones
- En lugar de reglas fijas, el agente decide en base a modelos de el mundo, objetivos y acciones
- Flexibilidad: al mismo agente se le 
pueden requerir objetivos distintos

### Diseño experimental

Se ejecutó un total de 30 veces cada algoritmo en escenarios aleatorios con las características descriptas en la introducción y se evaluó cada uno de los algoritmos sobre los mismos entornos generados. También se evaluó para el caso de un agente con comportamiento aleatorio

Se calculó la media y la desviación estándar de:
- Cantidad de estados explorados para llegar al objetivo (si es que fue posible) 
- Costo total de las acciones tomadas para las soluciones obtenidas 
- Tiempo empleado (segundos).

El agente aleatorio elige la acción a realizar al azar, siempre y cuando no haya un hueco. Esto incluye que puede pasar infinitas veces por el mismo lugar aunque ya lo haya explorado. Además, esta limitado a realizar como máximo 2000 movimientos, por lo que, en general, no encuentra el objetivo.
  
### Análisis y discusión de resultados

 A continuación, se presentan los resultados en gráficos de cajas y bigotes:

 ![Costo escenario 1:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp4-busquedas-informadas/images/Costo%20total%201_boxplot.png)

 En este gráfico, el costo 1 se refiere a la cantidad de movimientos que se realizó hasta llegar al objetivo. Podemos ver que, tanto el DFS como el DFS Limited, son los que más acciones toman hasta encontrar el objetivo. Y, por otro lado, tanto el BFS, UCS y A* toman menor cantidad de pasos hasta llegar al objetivo
 
 ![Costo escenario 2:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp4-busquedas-informadas/images/Costo%20total%202_boxplot.png)

 Este grafico, es similar al anterior, solo que al costo se le suma el número que representa la acción tomada (0 mueve a la izquierda, 1 mueve hacia abajo, 2 mueve a la derecha y 3 mueve hacia arriba). Se puede ver que los resultados son parecidos y el que varía sólo un poco es el agente aleatorio.

![Estados explorados:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp4-busquedas-informadas/images/Estados%20explorados_boxplot.png)

Podemos ver que tanto el DFS como el DFS Limited son los que menos estados exploraron, a pesar de que sus costos fueron los más altos anteriormente. Por otra parte, el BFS fue quien más estados exploró a quien le sigue el UCS y el A*


![Tiempo:](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp4-busquedas-informadas/images/Tiempo%20empleado_boxplot.png)

Finalmente, podemos ver que en relación al tiempo, los algoritmos A* y UCS son los más eficientes, y tanto DFS como DFS Limited los que mayor tiempo tardan.

A pesar de haber agregado a los gráficos los resultados del agente aleatorio, no tiene mucho sentido utilizarlo para realizar comparaciones debido a que tiene un límite en los movimientos, toma acciones sin ninguna lógica y por ultimo, la mayoría de las veces no llega al objetivo.

### Conclusiones

Como conclusión podemos ver que, dependiendo qué parámetro queremos optimizar, será el algoritmo que nos convenga utilizar. Para el caso del tiempo, nos conviene utilizar A* ya que es el más eficiente, o si no, UCS que tiene resultados parecidos.

Por otro lado, si necesitamos que se realicen la menor cantidad de movimientos (acciones) posibles, podríamos elegir tanto BFS, UCS, O A*. Y, en el caso de explorar la menor cantidad de celdas, elegiríamos DFS o DFS Limited.

Y, por último, en el caso del agente aleatorio, a pesar de haber agregado a los gráficos los resultados del agente aleatorio, no tiene mucho sentido utilizarlo para realizar comparaciones debido a que tiene un límite en los movimientos, toma acciones sin ninguna lógica y por ultimo, la mayoría de las veces no llega al objetivo.





