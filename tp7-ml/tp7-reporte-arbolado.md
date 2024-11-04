## **Informe sobre TP7 parte B**

### **A. Descripción del proceso de preprocesamiento**

1. **Eliminación de Variables**: 
   - En el proceso de **downsampling**, la variable inclinacion_peligrosa se excluye al crear un nuevo conjunto de datos balanceado (train_balanced). Sin embargo, no se eliminan otras variables.

2. **Manejo del Desbalanceo de Clases**: 
   - Se realiza un análisis de las clases en la variable inclinacion_peligrosa y se determina la proporción de la clase minoritaria. Si esta proporción es menor al 20%, se aplica **undersampling** mediante la función downSample del paquete caret, creando un conjunto de datos balanceado (train_balanced).

### B. Resultados Obtenidos sobre el Conjunto de Validación

- Se calcula el **AUC-ROC** (Área Bajo la Curva - Receiver Operating Characteristic) para evaluar el rendimiento del modelo. El resultado obtenido fue de 0.7553282

### C. Resultados Obtenidos en Kaggle

- La evaluación en Kaggle realizado con el conjunto de prueba (test_data) dió como resultado 0.69272, el cual supera el mínimo requerido de 0.69

### D. Descripción Detallada del Algoritmo Propuesto

1. **Carga de Datos**: 
   - Se cargan dos conjuntos de datos: uno para entrenamiento y otro para prueba.

2. **Preprocesamiento**:
   - Se transforma la variable inclinacion_peligrosa en un factor para asegurar que se trate como una variable categórica.
   - Se verifica el balanceo de clases y se aplica downsampling si es necesario.

3. **Entrenamiento del Modelo**:
   - Se entrena un modelo de **Random Forest** utilizando la función randomForest. 
   - Se crean 500 árboles en el bosque aleatorio, y se utilizan 3 variables al dividir en cada nodo.
   - Se calcula la importancia de las variables predictoras, lo cual es útil para entender qué variables son más relevantes para el modelo.

4. **Evaluación del Modelo**:
   - Se predicen las probabilidades para el conjunto de entrenamiento y se calcula la curva ROC.
   - Se imprime el AUC-ROC para evaluar el rendimiento del modelo.