# Informe del Proyecto ETL - Tratamiento y Carga de Datos desde Excel a SQLite

## Introducción

El presente informe detalla el desarrollo y la implementación de un proceso ETL para la extracción, transformación y carga de datos desde un archivo Excel proporcionado por el cliente hacia una base de datos SQLite. El proyecto se ha desarrollado utilizando Python para la automatización de tareas y ha abarcado desde la preparación de datos hasta la creación y población de tablas en la base de datos.

## Objetivos del Proyecto

El objetivo principal de este proyecto fue:
- Transformar los datos contenidos en el archivo Excel proporcionado por el cliente en una estructura adecuada para su posterior almacenamiento en una base de datos SQLite.

## Metodología

### Fase de Extracción

1. **Recepción del Archivo Excel:** Se elaboro un archivo Excel con datos IA a ser tratados y almacenados.

### Fase de Transformación

2. **Preparación y Limpieza de Datos:** 
   - Se cargaron los datos del archivo Excel en un DataFrame de Pandas.
   - Se realizaron procesos de limpieza, como la conversión de tipos de datos, manejo de valores nulos e inesperados, y normalización de datos.
   - Se aplicaron funciones de hash y transformaciones para la creación de claves únicas.

[![excelpi.png](https://i.postimg.cc/bwSVNLYG/excelpi.png)](https://postimg.cc/yDByLmZB)

3. **Diseño de la Base de Datos:**
   - Se definieron las tablas y sus relaciones utilizando SQLAlchemy.
   - Se crearon las estructuras de datos correspondientes para reflejar la estructura del modelo de datos.

### Fase de Carga

4. **Automatización del Proceso de Carga:**
   - Se estableció la conexión con la base de datos SQLite.
   - Se crearon las consultas SQL necesarias para insertar los datos tratados en las respectivas tablas.
   - Se verificó la inserción exitosa de los datos en la base de datos.

## Desafíos y Soluciones

[![tablanegocio.png](https://i.postimg.cc/L69MXcGJ/tablanegocio.png)](https://postimg.cc/K4HWpHGb)
### Desafíos Encarados

1. **Manipulación y Tratamiento de Datos Complejos:**
   - El archivo Excel contenía datos complejos y diversas inconsistencias que requerían una limpieza detallada y un tratamiento cuidadoso.

2. **Modelado y Normalización de Datos:**
   - Definir una estructura de base de datos que refleje de manera óptima la complejidad de los datos presentes en el archivo Excel.

### Soluciones Aplicadas

1. **Procesos de Limpieza y Normalización:**
   - Se desarrollaron funciones específicas en Python para tratar y limpiar los datos, asegurando consistencia y coherencia en la base de datos resultante.
   - Se aplicaron funciones de hash y transformaciones para garantizar la unicidad de las claves.

2. **Diseño Modular y Uso de Bibliotecas Específicas:**
   - Se utilizó la biblioteca Pandas para la manipulación y limpieza eficiente de los datos.
   - Se empleó SQLAlchemy para definir y modelar la estructura de la base de datos, permitiendo una implementación más ágil y robusta.

## Conclusiones y Resultados

El proyecto ha permitido transformar con éxito los datos del archivo Excel proporcionado por el cliente en una base de datos SQLite estructurada y apta para consultas y análisis posteriores. La automatización del proceso ETL garantiza la reutilización y escalabilidad del flujo de datos para futuras actualizaciones o nuevos conjuntos de datos.

---

