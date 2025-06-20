# pruebatecnicaanalista
Este repositorio contiene la solución de la prueba compartida para el puesto de Analista de Datos en PuntoRed. Se abordan 4 secciones,
la sección 1 corresponde a las preguntas teóricas, la sección 2 prueba técnica de sql, sección 3 prueba técnica de python y sección 4 la visualización de datos en Tableu.

## Sección 1: Preguntas Teóricas
####################
SQL
####################
1. JOIN: combina columnas de dos o más tablas relacionadas por un identificador o clave en común.

SELECT * FROM VENTAS AS A
JOIN PROVEEDORES AS B ON A.ID=B.IDPROV

  UNION: combina los resultados de dos consultas en una sola tabla, como su nombre lo dice une filas o registros siempre y cuando se tenga el mismo número y tipo de columnas

SELECT nombreproducto, id, ciudad FROM ventas
UNION
SELECT producto, idprov, ciudad FROM proveedores

2.- Una consulta CTE es una subconsulta definida por "WITH" la cual se puede reutilizar dentro de la consulta principal
Por ejemplo para obtener  las ciudades en las que mas se ha vendido 

WITH ventas_ciudad AS (
SELECT ciudad, SUM(monto) as Total
FROM VENTAS
GROUP BY  ciudad)

SELECT * FROM ventas_ciudad ORDER BY Total DESC

3.- HAVING: filtra filas después del GROUP BY, lo que ya se encuentra agregado mientras que WHERE filtra antes de agrupar 

4.- select cliente_id, sum(monto) as total
from ventas
group by cliente_id
having sum(monto) >250

#######################
Python
#######################

1.- Lista: es una colección ordenada de elementos , pueden ser de diferentes tipos y pueden haber elementos duplicados, van separados por comas

lista = [2,3,4,"hola",false]

  Diccionario: es una colección de pares que van de clave-valor en donde cada palabra (clave) tiene un significado (valor) asociado

diccionario = {"nombre": "Daniela", "edad": "28"}
si quisieramos ver el nombre de nuetsro diccionario se tendria que poner:
print(diccionario["nombre"]) obteniendo asi como resultado "Daniela"

2.- Pandas,numpy,matplotlib

3.- el código primero organizará la lista accediendo al penúltimo elemento por el [-2] que srría en este caso 5


#######################
Tableu
#######################

1.- Una dimensión es un campo cualitativo mientras que una medida es un valor numérico continuo que se puede agregar o calcular
2.- Si es un caso simple se podría utilizar un gráfico de pastel, sin embargo si se quiere visualizar mejor a más de 3-4 categorías sus porcentajes el ideal sería el de barras
3.-Tableu  permite elegir el tipo de filtro, para ello se debe de arrastrar el campo de fecha al área de filtros y ya en el dashboard actuvar dicha opción de mostrar el filtro
4.- Es un formato de archivo optimizado y comprimido que se utiliza para almacenar datos extraídos, se utiliza más cuando se tienen grandes volumenes o para optimizar el rendimiento sin
depender de la fuente original.


## Sección 2: Prueba Práctica SQL

1.- 
SELECT  departamento , AVG(salario) AS Sal_prom
FROM empleados
WHERE fecha_contratacion <= '2020-01-01'
GROUP BY departamento

2.-

SELECT TOP 5 b.id, b.nombre, b.apellido, SUM(a.monto) AS total_ventas
FROM ventas a
JOIN clientes b ON a.cliente_id = b.id
WHERE a.fecha >= DATEADD(MONTH, -6, GETDATE())
GROUP BY b.id, b.nombre, b.apellido
ORDER BY total_ventas DESC

3.-
SELECT b.id, b.nombre,b.apellido,AVG(a.monto) AS ticket_promedio
FROM ventas a
JOIN clientes b ON v.cliente_id = b.id
WHERE a.fecha >= DATEADD(YEAR, -1, GETDATE())
GROUP BY b.id, b.nombre, b.apellido

4.- 
SELECT CONCAT(a.nombre, ' ', a.apellido) AS nombre_completo, SUM(b.monto) AS total_ventas
FROM clientes a
JOIN ventas b ON a.id = b.cliente_id
GROUP BY a.id, a.nombre, a.apellido

5.-
SELECT DATETRUNC('month', fecha) AS mes, AVG(monto) AS ingreso_promedio
FROM ventas
GROUP BY mes
ORDER BY mes

6.-
WITH ventas_anuales AS (
  SELECT cliente_id, SUM(monto) AS total_ventas
  FROM ventas
  WHERE fecha >= DATEADD(YEAR, -1, GETDATE())
  GROUP BY cliente_id)
SELECT *,RANK() OVER (ORDER BY total_ventas DESC) AS ranking
FROM ventas_anuales

7.- 

WITH VentasPorCliente AS (
    SELECT c.id,c.nombre,c.apellido,SUM(v.monto) AS total_ventas
    FROM ventas v
    JOIN clientes c ON v.cliente_id = c.id
    WHERE v.fecha >= DATEADD(YEAR, -1, GETDATE())
    GROUP BY c.id, c.nombre, c.apellido)
SELECT vpc.id, vpc.nombre, vpc.apellido, vpc.total_ventas
FROM VentasPorCliente vpc
WHERE vpc.total_ventas > (SELECT AVG(total_ventas) FROM VentasPorCliente)

## Sección 3: Prueba Práctica python

1.-  Los 5 productos con mayor número de transacciones (cantidad_tx) son:

3 CLARO, 18 GB+MIN, 3 TIGO ,1415 30 GB+MIN ,574 60 GB+MIN


2.-  La categoría (proveedor) que más ingresos genera es: CLARO, con el mayor total en la columna valor_ventas.

3.- 
No se pudo realizar este análisis porque el archivo no incluye columnas para región ni canal, por lo tanto, no es posible responder esta pregunta con los datos proporcionados.







