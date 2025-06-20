import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carga del archivo CSV
df = pd.read_csv('ventas_operadores.csv')
df.columns = df.columns.str.strip()  # Limpia posibles espacios en los nombres de columna

# 2. Exploración básica
print("\nColumnas del archivo:")
print(df.columns)

print("\nPrimeros 5 registros:")
print(df.head())

print("\nInfo general del DataFrame:")
print(df.info())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nTipos de columnas:")
print(df.dtypes)

# 3. Limpieza de datos
df['fecha'] = pd.to_datetime(df['fecha'], dayfirst=True, errors='coerce')  # Convertir fechas
df = df.dropna(subset=['fecha'])  # Eliminar fechas no válidas
df = df.dropna()  # Eliminar cualquier otro registro con nulos

# 4. Análisis exploratorio

# Top 5 productos más vendidos por cantidad de transacciones
top_productos = df.groupby('producto')['cantidad_tx'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 productos más vendidos por unidades:")
print(top_productos)

# Proveedor que más ingresos genera
top_proveedores = df.groupby('proveedor')['valor_ventas'].sum().sort_values(ascending=False).head(5)
print("\nProveedor que más ingresos genera:")
print(top_proveedores)

# 5. Visualización: evolución de ventas mensuales
df['mes'] = df['fecha'].dt.to_period('M')
ventas_mensuales = df.groupby('mes')['valor_ventas'].sum()

ventas_mensuales.plot(kind='line', marker='o', title='Evolución de las ventas mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.tight_layout()
plt.show()

# Comparativo de ingresos y costos (suponiendo costo = 70% del valor)
df_categoria = df.groupby('proveedor')['valor_ventas'].sum().reset_index()
df_categoria['Costo_estimado'] = df_categoria['valor_ventas'] * 0.7
df_categoria.plot(x='proveedor', y=['valor_ventas', 'Costo_estimado'], kind='bar')
plt.title("Comparativo de Ingresos y Costos por Proveedor")
plt.ylabel("Monto")
plt.tight_layout()
plt.show()

# Gráfico de dispersión
# Crear columna de ganancia (ganancia = ingreso - costo estimado)
df['ganancia'] = df['valor_ventas'] * 0.3  # Si asumimos que el costo es 70%
plt.scatter(df['cantidad_tx'], df['ganancia'])
plt.xlabel("Número de ventas (transacciones)")
plt.ylabel("Ganancia")
plt.title("Relación entre número de ventas y ganancia")
plt.tight_layout()
plt.show()

# 6. Conclusiones del análisis
print("\nConclusiones:")
print("1. El producto más vendido por volumen es:", top_productos.idxmax())
print("2. El proveedor con más ingresos es:", top_proveedores.idxmax())
print("3. El mes con mayores ventas fue:", ventas_mensuales.idxmax(), "con un total de", ventas_mensuales.max())

# 7. Propuestas de mejora
print("\nPropuestas de mejora:")
print("- Priorizar los productos más vendidos en campañas promocionales.")
print("- Fortalecer la relación con el proveedor con mayor ingreso.")
print("- Analizar qué factores impulsaron las ventas en el mes pico para replicarlo.")
