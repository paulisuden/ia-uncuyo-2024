# **Ejercicio 2:**
 **A partir del archivo arbolado-mendoza-dataset-train.csv responder las siguientes preguntas:**

 a. **Cual es la distribución de las clase inclinacion_peligrosa?**

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp7-ml/code/intro/ej2/distribucion_inclinacion_peligrosa.png)

 b. **¿Se puede considerar alguna sección más peligrosa que otra?**

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp7-ml/code/intro/ej2/inclinacion_peligrosa_por_seccion.png)

 c. **¿Se puede considerar alguna especie más peligrosa que otra?**

![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp7-ml/code/intro/ej2/inclinacion_peligrosa_por_especie.png)

# **Ejercicio 3:**

1. **Generar un histograma de frecuencia para la variable circ_tronco_cm. Probar con diferentes números de bins.**
   
![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp7-ml/code/intro/ej3/histograma_circ_tronco_cm.png)

2. **Repetir el punto 1) pero separando por la clase de la variable inclinación_peligrosa?**
   
![](https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp7-ml/code/intro/ej3/histograma_circ_tronco_cm_inclinacion_peligrosa.png)

3. **Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo 4 posibles valores [ muy alto, alto, medio, bajo ]. Utilizar la información del punto b. para seleccionar los puntos de corte para cada categoría. Guardar el nuevo dataframe bajo el nombre de arbolado-mendoza-dataset-circ_tronco_cm-train.csv**

    Se encuentra en TP7-ML/data
https://github.com/paulisuden/ia-uncuyo-2024/blob/main/tp7-ml/data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv
