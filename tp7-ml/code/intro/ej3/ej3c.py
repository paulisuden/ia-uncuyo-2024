import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('data/arbolado-mendoza-dataset-train.csv')

plt.figure(figsize=(12, 6))

# con inclinación peligrosa
plt.subplot(1, 2, 1)
plt.hist(df_train[df_train['inclinacion_peligrosa'] == 1]['circ_tronco_cm'], bins=20, color='salmon', edgecolor='black')
plt.title('Circunferencia del Tronco (inclinación peligrosa)')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

# sin inclinación peligrosa
plt.subplot(1, 2, 2)
plt.hist(df_train[df_train['inclinacion_peligrosa'] == 0]['circ_tronco_cm'], bins=20, color='pink', edgecolor='black')
plt.title('Circunferencia del Tronco (inclinación no peligrosa)')
plt.xlabel('Circunferencia del tronco (cm)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.savefig('histograma_circ_tronco_cm_inclinacion_peligrosa.png')
plt.show()


