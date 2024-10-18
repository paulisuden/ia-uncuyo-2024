import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('data/arbolado-mendoza-dataset-train.csv')

plt.figure(figsize=(12, 6))


#puntos de corte 
bins = [0, 30, 60, 90, df_train['circ_tronco_cm'].max()]
labels = ['bajo', 'medio', 'alto', 'muy alto']

#crear la columna
df_train['circ_tronco_cm_cat'] = pd.cut(df_train['circ_tronco_cm'], bins=bins, labels=labels, include_lowest=True)


df_train.to_csv('data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv', index=False)

print("Nuevo archivo guardado con la columna 'circ_tronco_cm_cat'.")
