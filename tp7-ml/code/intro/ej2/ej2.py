import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trainDataSet = pd.read_csv('data/arbolado-mendoza-dataset-train.csv')

sns.set_theme(style="darkgrid")

#distribución de la clase inclinacion_peligrosa
plt.figure(figsize=(8, 6))
sns.countplot(x='inclinacion_peligrosa', data=trainDataSet) #* sns.countplot genera grafico de barra
plt.title('Distribución de la inclinación peligrosa')
plt.xlabel('Inclinación peligrosa')
plt.ylabel('Cantidad')
plt.savefig('distribucion_inclinacion_peligrosa.png')
plt.show()

# b. se puede considerar alguna sección más peligrosa que otra?
plt.figure(figsize=(10, 6))
sns.countplot(x='seccion', hue='inclinacion_peligrosa', data=trainDataSet)
plt.title('Inclinación peligrosa por sección')
plt.xlabel('Sección')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.legend(title='Inclinación peligrosa')
plt.savefig('inclinacion_peligrosa_por_seccion.png')
plt.show()

# c. se puede considerar alguna especie más peligrosa que otra?
plt.figure(figsize=(12, 6))
# filtra las 10 especies mas repetidas
common_species = trainDataSet['especie'].value_counts().nlargest(10).index #solo se queda con los nombres y cantidad
#elige aquellos que esten en las especies comunes
filtered_df = trainDataSet[trainDataSet['especie'].isin(common_species)]

sns.countplot(x='especie', hue='inclinacion_peligrosa', data=filtered_df)
plt.title('Inclinación peligrosa por especie (Top 10 especies)')
plt.xlabel('Especie')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.legend(title='Inclinación peligrosa')
plt.savefig('inclinacion_peligrosa_por_especie.png')
plt.show()

