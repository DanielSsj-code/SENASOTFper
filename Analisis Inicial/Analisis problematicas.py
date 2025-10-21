import pandas as pd
import numpy as np
import unicodedata 
from pathlib import Path

# usar la carpeta del script para construir rutas absolutas
base_dir = Path(__file__).resolve().parent
file_name = base_dir / 'dataset_comunidades_senasoft.csv'
output_file_name = base_dir / 'normalized_data_comunidades_senasoft.csv'

try:
    df = pd.read_csv(file_name)
except FileNotFoundError:
    print(f"Error: El archivo '{file_name}' no fue encontrado.")
    print("Directorio de trabajo actual:", Path.cwd())
    # listar algunos archivos del directorio del script para depurar
    print("Archivos en el directorio del script:", [p.name for p in base_dir.iterdir()][:50])
    raise

# --- NUEVA FUNCIÓN PARA NORMALIZAR VALORES DE TEXTO (manejo de tildes) ---
def normalize_text_value(text):
    """
    Elimina tildes y otros acentos, convierte el texto a minúsculas y elimina espacios 
    extras para asegurar consistencia en los valores categóricos (ej. 'Medellín' -> 'medellin').
    """
    if pd.isna(text):
        return text 
    
    text = str(text).strip()
    
    # Normalización NFKD y eliminación de acentos mediante codificación/decodificación a ascii
    normalized = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    
    return normalized.lower()

# --- 2. TRANSFORMACIÓN (T: Transform) - NORMALIZACIÓN Y LIMPIEZA ---

# 2.1 Estandarización de Nombres de Columnas
def standardize_column_names(df):
    """Convierte los nombres de las columnas a snake_case."""
    new_columns = []
    for col in df.columns:
        new_col = col.lower().replace(' ', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
        new_columns.append(new_col)
    df.columns = new_columns
    return df

df = standardize_column_names(df)

# 2.2 Conversión de Tipos de Datos (Dtypes)
df['fecha_del_reporte'] = pd.to_datetime(df['fecha_del_reporte'], errors='coerce')

# 2.3 Manejo de Valores Faltantes (NaN) - Imputación
median_edad = df['edad'].median()
df['edad'] = df['edad'].fillna(median_edad).astype(int)
df['genero'] = df['genero'].fillna('Desconocido')
df['ciudad'] = df['ciudad'].fillna('Desconocido')
df['comentario'] = df['comentario'].fillna('Sin Comentario')

# 2.4 Estandarización de Texto para Categorías y Texto Libre
# ¡CORRECCIÓN! Se incluye 'comentario' para asegurar que el texto libre tampoco tenga tildes.
text_cols = ['nombre', 'genero', 'ciudad', 'categoria_del_problema', 'nivel_de_urgencia', 'comentario']
for col in text_cols:
    df[col] = df[col].apply(normalize_text_value)
# 2.5 Eliminación de duplicados
df.drop_duplicates(inplace=True)

# --- 3. CARGA (L: Load) ---
df.to_csv(output_file_name, index=False)