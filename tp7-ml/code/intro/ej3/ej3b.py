import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('data/arbolado-mendoza-dataset-train.csv')

# Generar histogramas con diferentes números de bins
plt.figure(figsize=(8, 6))

#10 bins
plt.subplot(2, 2, 1)
plt.hist(df_train['circ_tronco_cm'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma con 10 bins')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

#20 bins
plt.subplot(2, 2, 2)
plt.hist(df_train['circ_tronco_cm'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Histograma con 20 bins')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

#30 bins
plt.subplot(2, 2, 3)
plt.hist(df_train['circ_tronco_cm'], bins=30, color='pink', edgecolor='black')
plt.title('Histograma con 30 bins')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

#50 bins
plt.subplot(2, 2, 4)
plt.hist(df_train['circ_tronco_cm'], bins=50, color='salmon', edgecolor='black')
plt.title('Histograma con 50 bins')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

# Mostrar los gráficos
plt.tight_layout()
plt.savefig('histograma_circ_tronco_cm.png')
plt.show()
