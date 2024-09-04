 ## **Introducción: descripción general del problema**
 En los ejercicios 4 y 5, lo que se debe hacer es evaluar el desempeño del agente reflexivo (punto 4), y de un agente aleatorio (punto 5). Esto es medida de desempeño y unidades de tiempo
 consumidas, para:
 - Entornos de: 2×2, 4×4, 8×8, 16×16, 32×32, 64×64, 128×128.
 - Porcentaje de suciedad en el ambiente: 0.1, 0.2, 0.4, 0.8

## **Marco teórico: descripción teórica y general del funcionamiento del entorno y de los agentes, y sus principales elementos.**
Primero los agentes son entidades que perciben el entorno a través de sensores y actúan sobre él mediante actuadores. Su objetivo es maximizar alguna forma de rendimiento o cumplir una tarea específica. Por otro lado, un entorno es el espacio donde los agentes operan e interactúan. El entorno puede ser determinista o estocástico, observable o parcialmente observable, estático o dinámico, entre otros. 

Los agentes aleatorios toman decisiones al azar, sin seguir un criterio definido o lógico basado en las percepciones del entorno. Es decir, no poseen una estrategia de toma de decisiones optimizada. Dado que sus acciones no dependen de un análisis del entorno, no se garantiza que sus acciones sean adecuadas o que logren su objetivo de manera eficiente.

Los agentes reflexivos simples toman decisiones basadas únicamente en la percepción actual del entorno, sin considerar el historial de interacciones o el estado interno. Son modelos simplificados que contienen ciertas limitaciones como por ejemplo que no consideran secuencia de percepciones y no pueden estimar lo que no perciben.

## **Diseño experimental: descripción de los experimentos, es decir, descripción de la medida de rendimiento, de las diferentes configuraciones del entorno (tamaño y porcentaje de suciedad), cantidad de repeticiones.**

En el experimento, como se explicó en la introducción, dados los entornos y porcentajes de suciedad en el ambiente, lo que se hizo fue combinar cada uno de estos entornos con las suciedades. Por ejemplo, para el entorno 2x2 se tomó la medida de desempeño para las distintas suciedades dadas: 0.1, 0.2, 0.4 y 0.8.

El agente en cada entorno y cada suciedad, realizó un total de 1000 acciones, en las cuales se contó cuántas veces limpió en total. A la vez, este procedimiento se repitió 10 veces, con un entorno distinto cada vez. Por último, se promedió la cantidad total de veces que se limpió en esas 10 combinaciones. Así es como encontramos los valores que luego veremos en los gráficos.

Esto, se realizó en simultáneo con el agente aleatorio y el reflexivo simple. Por lo que ambos realizaron el experimento en los mismos entornos. Esto ayuda a comparar correctamente los resultados obtenidos en el experimento.

Básicamente, la diferencia entre un agente aleatorio y uno reflexivo simple es que, el primero sólo limpia cuando la acción que le toque sea "limpiar" y, además, que en la celda donde se encuentre, esté sucia. Con cualquier otra acción que le toque, NO limpia. Por otro lado, el agente reflexivo, siempre va a tener una percepción de la celda en la que se encuentra, y si la misma está sucia, la limpiará, y en caso contrario, realizará algún movimiento y volverá a limpiar de ser necesario.

## **Análisis y discusión de resultados: presentar los resultados obtenidos en los experimentos, realizando un breve análisis de dichos resultados, e incluyendo gráficas o tablas que los resuman.**

En las siguientes imágenes, se pueden ver los resultados obtenidos del experimento realizado.
![Agente Reflexivo](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp2-agentes-racionales/images/agente%20reflexivo.png)
![Agente Aleatorio](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp2-agentes-racionales/images/agente%20aleatorio.png)

Podemos ver un ejemplo concreto del caso del entorno de tamaño 4x4 y suciedad 0.4 en la combinación número 1:
![Entorno 4x4 suciedad 0.4](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp2-agentes-racionales/images/Captura%20de%20pantalla%202024-08-22%20112144.png)

Como vemos, los valores son números comprendidos entre 0 y 1. En cada caso, una celda se considera sucia, si su valor es mayor o igual al porcentaje de suciedad en ese instante. En este caso, estarían sucias aquellas celdas en las que el valor es mayor o igual a 0.4 como por ejemplo, 0.53 y 0.46

Dicho esto, y analizando los resultados obtenidos con ambos agentes en los mismos entornos, podemos ver que un agente reflexivo simple es mucho más eficiente que un agente aleatorio.

## **Conclusiones finales de los resultados obtenidos.**

Como conclusión, podemos decir que un agente reflexivo simple es mucho más eficiente que un agente aleatorio. Esto es debido a que el aleatorio actúa sin ninguna lógica o reglas, eligiendo acciones de manera completamente al azar, mientras que el reflexivo sigue reglas predefinidas que asocian una acción específica con una percepción particular del entorno. En este caso, si percibe que donde se encuentra hay suciedad, activará una regla que le dice que debe limpiar.
