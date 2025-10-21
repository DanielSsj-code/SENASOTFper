import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURACIÓN DE ARCHIVOS ---
INPUT_FILE = "Analisis Inicial/dataset_comunidades_senasoft.csv"
OUTPUT_FILE_TRANSFORMADO = "normalized_data_comunidades_senasoft.csv"

print(f"Iniciando proceso ETL y generación de gráficas con el archivo: {INPUT_FILE}")

# ====================================
# PASO 1: EXTRACCIÓN Y TRANSFORMACIÓN (ETL)
# ====================================

try:
    # 1. Extracción (E)
    df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo '{INPUT_FILE}'. Asegúrate de que esté en la misma carpeta.")
    exit()

# 2. Transformación (T)
# 2.1 Estandarización de nombres de columnas a snake_case (minúsculas y guiones bajos)
df.columns = [
    'id', 'nombre', 'edad', 'genero', 'ciudad', 'comentario',
    'categoria_del_problema', 'nivel_de_urgencia', 'fecha_del_reporte',
    'acceso_a_internet', 'atencion_previa_del_gobierno', 'zona_rural'
]

# 2.2 Cálculo de valores para imputación
median_age = df['edad'].median()
mode_gender = df['genero'].mode()[0]
mode_city = df['ciudad'].mode()[0]

# 2.3 Imputación de Valores Faltantes
df['comentario'] = df['comentario'].fillna('Sin Comentario')
df['edad'] = df['edad'].fillna(median_age).astype(int)
df['genero'] = df['genero'].fillna(mode_gender)
df['ciudad'] = df['ciudad'].fillna(mode_city)

# 2.4 Conversión de Tipos de Datos y Feature Engineering
df['fecha_del_reporte'] = pd.to_datetime(df['fecha_del_reporte'], format='%Y-%m-%d')
df['año_del_reporte'] = df['fecha_del_reporte'].dt.year
df['mes_del_reporte'] = df['fecha_del_reporte'].dt.month

# 2.5 Eliminar columna de fecha original
df = df.drop(columns=['fecha_del_reporte'])

# 3. Carga (L)
df.to_csv(OUTPUT_FILE_TRANSFORMADO, index=False)
print(f"\n[ÉXITO ETL] DataFrame limpio y transformado guardado en: {OUTPUT_FILE_TRANSFORMADO}")

