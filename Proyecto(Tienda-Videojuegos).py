import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pyodbc

# Establecer estilos para los gráficos
plt.style.use('ggplot')  # Usar el estilo de ggplot para gráficos
sns.set_style("dark")  # Establecer un estilo oscuro para gráficos de Seaborn

# Leer el archivo de Excel con datos de videojuegos
df = pd.read_excel("/Users/aquin/OneDrive/Documentos/Python.com/Tienda-Videojuegos.xlsx")

# Mostrar las primeras 11 filas del DataFrame
df.head(11)

# Mostrar las últimas 11 filas del DataFrame
df.tail(11)

# Mostrar la información del DataFrame: columnas, tipos de datos y no nulos
df.info()

# Resumen estadístico del DataFrame: contar, media, desvío, min, max, etc.
df.describe()

# Contar el número de filas duplicadas en el DataFrame
df.duplicated().sum()

# Contar el número de valores nulos por columna
df.isnull().sum()

# Rellenar los valores nulos con la media en las columnas numéricas
df = df.fillna(df.mean(numeric_only = True))

# Rellenar los valores nulos en la columna "Región" con la etiqueta "Desconocida"
df["Región"] = df["Región"].fillna("Desconocida")

# Rellenar los valores nulos en la columna "Fecha de Lanzamiento" con "Fecha-Desconocida"
df["Fecha de Lanzamiento"] = df["Fecha de Lanzamiento"].fillna("Fecha-Desconocida")

# Eliminar las filas con valores nulos restantes
df.dropna(axis = 0, inplace = True)

# Eliminar las columnas que contienen valores nulos
df.dropna(axis = 1, inplace = True)

# Crear un gráfico de barras comparando los títulos y el número de reseñas
fig, ax = plt.subplots(facecolor="lightgrey", figsize=(15, 8))  # Crear la figura y ajustar el tamaño

# Asignar colores: azul para todos y rojo para el cuarto título
color = ["blue"] * len(df)
color[4] = "red"

# Crear el gráfico de barras con los colores asignados
plt.bar(df["Título"], df["Número de Reseñas"], edgecolor="black", color=color)

# Añadir leyendas para distinguir el título con más reseñas
plt.bar(df["Título"], df["Número de Reseñas"], edgecolor="black", color="blue", label="Otro Título")
plt.bar(df["Título"].iloc[4], df["Número de Reseñas"].iloc[4], edgecolor="black", color="red", label="Título con Más Reseñas")

# Configurar título y etiquetas del gráfico
plt.title("Comparación de Títulos por Número de Reseñas", color="darkblue", fontweight="bold", x=0.5, y=1)
plt.xlabel("Título del Videojuego", color="darkblue", fontweight="bold", fontsize = 11)
plt.ylabel("Número de Reseñas", color="darkblue", fontweight="bold", fontsize = 11)

# Configurar rotación y estilo de los ticks en el eje x
plt.xticks(rotation=25, ha="right", fontsize=8, color="black", fontweight="bold")
plt.yticks(color="black", fontweight="bold", fontsize=8)

# Añadir leyenda, cuadrícula, y ajustar el diseño
plt.legend(title="Comparación por Reseñas", loc="best", facecolor="white")
plt.grid(True, color="grey", linestyle="--")
plt.tight_layout()  # Ajusta automáticamente el espacio del gráfico
plt.show()

# Crear un gráfico de líneas que muestre la evolución de versiones en función de la fecha de adquisición
fig , ax = plt.subplots(facecolor = "lightgrey", figsize = (11,7))

# Graficar los datos con marcadores y líneas discontinuas
plt.plot(df["Fecha de Adquisición"], df["Versión"], marker = "o", linestyle = "--", color = "red", label = "Versiones de Productos")

# Añadir título y etiquetas
plt.title("Evolución de las Versiones de Productos en Función de la Fecha de Adquisición", color = "darkblue", fontweight = "bold")
plt.xlabel("Fecha de Adquisición", color = "darkblue", fontweight = "bold")
plt.ylabel("Versión del Producto", color = "darkblue", fontweight = "bold")

# Configurar ticks en los ejes
plt.xticks(color = "black", fontweight = "bold")
plt.yticks(color = "black", fontweight = "bold")

# Añadir cuadrícula y leyenda
plt.grid(True, color = "grey", linestyle = "-", alpha = 0.2)
plt.legend(loc = "best", facecolor = "white")
plt.tight_layout()
plt.show()

# Crear gráficos de pastel comparando distribución por Plataforma y Género
fig, (ax1, ax2) = plt.subplots(1, 2, facecolor="lightgrey", figsize=(15, 9))

# Contar la cantidad de juegos por plataforma
estado_counts = df["Plataforma"].value_counts()

# Contar la cantidad de juegos por género
estado_counts2 = df["Género"].value_counts()

# Crear gráfico de pastel para plataformas
ax1.pie(estado_counts, labels = estado_counts.index, shadow = True, autopct = "%1.1f%%")
ax1.set_title("Distribución de Juegos por Plataforma", color = "darkblue", fontweight = "bold")
ax1.legend(labels = estado_counts.index, loc = "lower left", facecolor = "white", bbox_to_anchor = (1,0), title = "Plataformas")

# Crear gráfico de pastel para géneros
ax2.pie(estado_counts2, labels = estado_counts2.index, shadow = True, autopct = "%1.1f%%")
ax2.set_title("Distribución de Juegos por Género", color="darkblue", fontweight="bold")
ax2.legend(estado_counts2, loc = "lower right", facecolor = "white", bbox_to_anchor = (1.2,0), title = "Genero")

# Ajustar el espacio entre gráficos y mostrar la visualización
plt.subplots_adjust(wspace = 0.7)
plt.show()
