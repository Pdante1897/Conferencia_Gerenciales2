import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('amazon/Musical_instruments_reviews.csv')

# Manejo de valores faltantes
df = df.dropna()  # Eliminar filas con valores faltantes
df = df.fillna(0)  # Rellenar valores faltantes con ceros

# Eliminación de duplicados
df = df.drop_duplicates()

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Mostrar información sobre el DataFrame
print("\nInformación sobre el DataFrame:")
print(df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Filtrar el DataFrame por una condición
print("\nReseñas con una calificación mayor a 4:")
reseñas_buenas = df[df['overall'] > 4]
print(reseñas_buenas)

# Contar el número de reseñas por revisor
conteo_reseñas_por_revisor = df['reviewerID'].value_counts()
print("\nConteo de reseñas por revisor:")
print(conteo_reseñas_por_revisor.head())
