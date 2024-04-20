import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('archive/train.csv')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Mostrar información sobre el DataFrame
print("\nInformación sobre el DataFrame:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Visualización de datos

# Histograma de la popularidad
plt.figure(figsize=(8, 6))
plt.hist(df['Popularity'], bins=20, color='skyblue')
plt.title('Distribución de la popularidad de las canciones')
plt.xlabel('Popularidad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Gráfico de dispersión de danceability vs. energy
plt.figure(figsize=(8, 6))
plt.scatter(df['danceability'], df['energy'], color='green', alpha=0.7)
plt.title('Danceability vs. Energy')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True)
plt.show()
