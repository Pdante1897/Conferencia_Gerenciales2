import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('spotify/spotipyMusicGenres.csv')

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

# Histograma de la danceability
plt.figure(figsize=(8, 6))
plt.hist(df['danceability'], bins=20, color='skyblue')
plt.title('Distribución de la danceability de las canciones')
plt.xlabel('Danceability')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Gráfico de dispersión de energy vs. tempo
plt.figure(figsize=(8, 6))
plt.scatter(df['energy'], df['tempo'], color='green', alpha=0.7)
plt.title('Energy vs. Tempo')
plt.xlabel('Energy')
plt.ylabel('Tempo')
plt.grid(True)
plt.show()
