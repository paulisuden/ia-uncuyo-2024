## **6. Responder las preguntas 2.10 y 2.11 de AIMA 3ra Edición**
### **2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.**
#### **a. Can a simple reflex agent be perfectly rational for this environment? Explain.**
No,  un agente no sería racional si este es penalizado un punto por cada movimiento, ya que el mismo se mueve infinitamente, encuentre o no suciedad, por lo que sería penalizado todo el tiempo. Entonces, no sería racional, no maximizaría la medida de desempeño. Esto es debido a que no tiene memoria respecto de los cuadrados sucios por los que pasó, y además no conoce de antemano el entorno en el que se encuentra.
#### **b. What about a reflex agent with state? Design such an agent.**
Si guardara información sobre el estado actual en el que se encuentra y los cuadrados sucios por los que pasó, aun así, no conocería el entorno en su totalidad, por lo que no sería racional.
#### **c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?**
En este caso, el agente sí sería racional, ya que conocería el estado en que se encuentra cada cuadrado, y solo realizaría movimientos en caso de ser necesario (que un cuadrado esté sucio).
### **2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)** 
#### **a. Can a simple reflex agent be perfectly rational for this environment? Explain.**
Un agente de reflejo simple no sería racional en este entorno ya que no tiene “memoria”, no puede estimar lo que no percibe, además de que toma decisiones únicamente basadas en su percepción inmediata. Por otro lado, no tendría conocimiento previo del entorno (extensión, límites, etc.) y esto podría hacer que realice un recorrido sumamente ineficiente dejando áreas del entorno sin explorar, por ejemplo.
#### **b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.** 
Como se puede ver en los resultados obtenidos en los ejercicios 4 y 5, un agente aleatorio no tiene mejor rendimiento que un agente reflexivo simple. 
#### **c. Can you design an environment in which your randomized agent will perform poorly? Show your results.**
Un agente aleatorio seguramente tenga un rendimiento pobre en un entorno en el que la probabilidad de que un casillero esté sucio sea baja, pero también, en un entorno con un tamaño muy grande, debido a la baja probabilidad de que el agente pase por un casillero sucio.
#### **d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?**
Sí, un agente basado en reflejos con estado puede superar a un agente simple basado en reflejos, ya que un agente con estado tiene la capacidad de recordar lo que ha hecho y dónde ha estado, lo que le permite tomar decisiones más informadas y no volver a pasar por el mismo camino.
