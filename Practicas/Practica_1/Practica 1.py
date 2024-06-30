#   Instalación de librerias
#   pip install pandas
#   pip install matplotlib
#   pip install seaborn

#   Librerias
import pandas as pd

#   Carga de información - Prework
url = "https://raw.githubusercontent.com/karimacuna2008/Clase_Aprendizaje_Automatico/main/Practicas/Practica_1/typed_uanl.csv"
df = pd.read_csv(url)
print(df.describe())

#   Estadísticas descriptivas
for columna in df.columns:
    descripcion = df[columna].describe()
    print(f"Estadísticas descriptivas de '{columna}':")
    print(descripcion)
    print()

