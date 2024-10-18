import pandas as pd #* cargar y manipular los datos
from sklearn.model_selection import train_test_split #* dividir el conjunto de datos de manera aleatoria y uniforme

dataSet = pd.read_csv('arbolado-mza-dataset.csv')

# dividir
trainDataSet, validationDataSet = train_test_split(dataSet, test_size=0.2, random_state=42)

trainDataSet.to_csv('arbolado-mendoza-dataset-train.csv', index=False) #no incluir indices de las filas
validationDataSet.to_csv('arbolado-mendoza-dataset-validation.csv', index=False)

print("archivos generados")
