## **Reporte TP 7**

### **1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.**
   
- **The sample size n is extremely large, and the number of predictors p is small.**

    En este escenario, podríamos esperar que un método inflexible capture los patrones de los datos de una mejor que un método flexible, ya que el segundo podría caer en overfitting.

- **The number of predictors p is extremely large, and the number of observations n is small.**

    Un método flexible sería mejor que un método inflexible, ya que el primero sería más capaz de capturar relaciones complejas en los datos.

- **The relationship between the predictors and response is highly non-linear.**
  
    Si la relación entre los predictores es altamente no-lineal, un método flexible sería mejor ya que estos, como los modelos no lineales, pueden capturar relaciones no lineales de manera más efectiva, mientras que los métodos inflexibles podrían tener dificultades para modelar estos tipos de patrones
 
- **The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.**
  
     Si sabemos que el error irreducible es muy alto, no sería conveniente utilizar un método muy flexible ya que este podría realizar overfitting sobre los datos

### **2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.**

- **We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.**

Tipo de Problema: Regresión.

Interés: Inferencia, entender la relación entre los factores y el salario del CEO.

n = 500 y p = 4
  
- **We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.**

Tipo de Problema: Clasificación.

Interés: Predicción

n = 20 y p = 14
  
- **We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.**

Tipo de Problema: Regresión.

Interés: Predicción

n = 52 (semanas) y p = 4

### **5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what  circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?**

Ventajas de un enfoque muy flexible:

1. **Captura de Relaciones Complejas**: Puede modelar patrones no lineales y relaciones intrincadas en los datos, lo que lo hace adecuado cuando la relación entre los predictores y la respuesta es complicada.
   
2. **Mayor Precisión en Datos Complejos**: Cuando la relación subyacente es difícil de modelar con enfoques más simples, un método flexible puede ajustarse mejor a los datos, proporcionando una mayor precisión en los resultados.

3. **Adaptabilidad a Cambios**: Los modelos flexibles, como las redes neuronales o los árboles de decisión con muchos nodos, pueden adaptarse a patrones dinámicos y cambiantes, siendo útiles en sistemas que evolucionan rápidamente.

Desventajas de un enfoque muy flexible:

1. **Sobreajuste (Overfitting)**: Dado que los modelos flexibles pueden ajustarse muy bien a los datos de entrenamiento, corren el riesgo de capturar ruido y detalles irrelevantes, lo que puede llevar a un peor rendimiento en datos nuevos.
   
2. **Menor Interpretabilidad**: Estos modelos son más difíciles de interpretar, lo que puede ser un problema en situaciones donde la comprensión y explicación del modelo son esenciales, como en el ámbito médico o financiero.

3. **Mayor Costo Computacional**: Los métodos flexibles suelen requerir más recursos computacionales y pueden ser más lentos de entrenar y ejecutar.

Enfoque menos flexible:

Este puede ser preferible cuando:

1. **Interpretabilidad**: Si se requiere entender y explicar el modelo fácilmente, como en aplicaciones regulatorias o de toma de decisiones, un método menos flexible como la regresión lineal es más útil.
   
2. **Menor Riesgo de Sobreajuste**: En escenarios con pocos datos o datos ruidosos, los modelos menos flexibles tienen menos riesgo de sobreajustarse, lo que mejora su capacidad de generalización.

3. **Simplicidad y Eficiencia**: Los enfoques menos flexibles tienden a ser más simples y computacionalmente más eficientes, lo que es ideal cuando se tienen recursos limitados o se necesita rapidez en el procesamiento.

### Conclusión:
- **Enfoque flexible**: Elegirlo cuando la relación entre los predictores y la respuesta es compleja o no lineal, cuando tenemos grandes cantidades de datos y el objetivo principal es la precisión en la predicción.
  
- **Enfoque menos flexible**: Elegirlo cuando se requiere interpretabilidad, hay pocos datos disponibles o si la relación entre los predictores y la respuesta es relativamente sencilla.

### **6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are its disadvantages?**

Un enfoque paramétrico asume una forma fija y conocida para la función que relaciona los predictores y la respuesta. Por ejemplo, una línea o un polinomio. De forma que se estiman los parámetros de la forma asumida.

En cambio, un enfoque no paramétrico no hace ninguna suposición sobre la forma de la función y trata de aprenderla directamente de los datos.

**Ventajas de un enfoque paramétrico:**

- Es más simple y rápido de ajustar que un enfoque no paramétrico.

- Requiere menos datos para estimar los parámetros de la función.

- Permite hacer inferencia sobre los efectos de los predictores sobre la respuesta.

**Desventajas de un enfoque paramétrico:**

- Puede tener un alto sesgo si la forma asumida para la función no se ajusta a la realidad.

- Puede perder información relevante al ignorar aspectos de los datos que no se ajustan al modelo.

### **7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.**

| Obs. |  X1 |  X2 |  X3 |  X4   |
|------|-----|-----|-----|-------|
|  1   |  0  |  3  |  0  |  Red  |
|  2   |  2  |  0  |  0  |  Red  |
|  3   |  0  |  1  |  3  |  Red  |
|  4   |  0  |  1  |  2  | Green |
|  5   | -1  |  0  |  1  | Green |
|  6   |  1  |  1  |  1  |  Red  |

### **Suppose we wish to use this data set to make a prediction for Y when X1=X2=X3=0 using K-nearest neighbors.**

- **Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 =0.**

  1. d((0,0,0), 1) = 3
  2. d((0,0,0), 2) = 2
  3. d((0,0,0), 3) = 3.16
  4. d((0,0,0), 4) = 2.23
  5. d((0,0,0), 5) = 1.41
  6. d((0,0,0), 6) = 1.73
  
- **What is our prediction with K =1? Why?**
  
  La prediccion es igual a la clase del vecino más cercano (verde).
  
- **What is our prediction with K = 3? Why?**

    La predicción es rojo, debido a que dos tercios de sus vecinos más cercanos tienen esa clase.
  
- **If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?**

    En ese caso, esperamos que el mejor valor de K sea pequeño, ya que la mayor varianza permite darle a la frontera una forma no lineal