# ====================================
# PASO 2: GENERACIÓN DE GRÁFICAS (INFORME INICIAL)
# ====================================

# Configuración de Matplotlib y Seaborn
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
filenames = []

# --- GRÁFICA 1: CATEGORÍA DEL PROBLEMA ---
plt.figure()
data = df['categoria_del_problema'].value_counts()
sns.barplot(x=data.index, y=data.values, palette="plasma")
plt.xlabel("Categoría del Problema")
plt.ylabel("Conteo de Reportes")
plt.title("1. Distribución de Reportes por Categoría del Problema")
plt.tight_layout()
plt.savefig('1_categoria_problema_distribucion.png')
plt.close()
filenames.append('1_categoria_problema_distribucion.png')

# --- GRÁFICA 2: NIVEL DE URGENCIA ---
plt.figure()
data = df['nivel_de_urgencia'].value_counts()
sns.barplot(x=data.index, y=data.values, palette="viridis")
plt.xlabel("Nivel de Urgencia")
plt.ylabel("Conteo de Reportes")
plt.title("2. Distribución de Reportes por Nivel de Urgencia")
plt.tight_layout()
plt.savefig('2_nivel_urgencia_distribucion.png')
plt.close()
filenames.append('2_nivel_urgencia_distribucion.png')

# --- GRÁFICA 3: TOP 5 CIUDADES ---
plt.figure()
# Obtener las 5 ciudades con más reportes
top_data = df['ciudad'].value_counts().nlargest(5)
sns.barplot(x=top_data.index, y=top_data.values, palette="mako")
plt.xlabel("Ciudad (Top 5)")
plt.ylabel("Conteo de Reportes")
plt.title("3. Top 5 Ciudades con Mayor Número de Reportes")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('3_ciudad_top5_distribucion.png')
plt.close()
filenames.append('3_ciudad_top5_distribucion.png')

# --- GRÁFICA 4: ZONA RURAL vs. URBANA ---
plt.figure()
# Mapear 0 y 1 a etiquetas descriptivas
zona_data = df['zona_rural'].map({0: 'Urbana (0)', 1: 'Rural (1)'}).value_counts()
sns.barplot(x=zona_data.index, y=zona_data.values, palette="magma")
plt.xlabel("Zona (0=Urbana, 1=Rural)")
plt.ylabel("Conteo de Reportes")
plt.title("4. Distribución de Reportes por Zona")
plt.tight_layout()
plt.savefig('4_zona_rural_distribucion.png')
plt.close()
filenames.append('4_zona_rural_distribucion.png')

print("\n[ÉXITO GRÁFICAS] Las gráficas de barras para el informe inicial han sido generadas:")
for f in filenames:
    print(f"- {f}")
print("\nEl proceso ha finalizado. Puedes encontrar el CSV transformado y las imágenes en tu carpeta.")