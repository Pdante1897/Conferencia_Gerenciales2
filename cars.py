import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('cars/Car_sales.csv')

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
import matplotlib.pyplot as plt

# Histograma de las ventas en miles
plt.figure(figsize=(8, 6))
plt.hist(df['Sales_in_thousands'], bins=20, color='skyblue')
plt.title('Distribución de ventas en miles')
plt.xlabel('Ventas en miles')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Gráfico de dispersión de precio vs. horsepower
plt.figure(figsize=(8, 6))
plt.scatter(df['Price_in_thousands'], df['Horsepower'], color='green', alpha=0.7)
plt.title('Precio vs. Caballos de fuerza')
plt.xlabel('Precio (en miles)')
plt.ylabel('Caballos de fuerza')
plt.grid(True)
plt.show()
