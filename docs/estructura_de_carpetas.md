# Estructura de Directorios

## Overview
Este documento describe la organización de directorios y archivos. Sirve como guía para navegar y comprender la estructura del proyecto.

### Cómo Actualizar Este Documento
Al agregar nuevos dirs o realizar cambios significativos en la estructura de dirs, actualice este documento para mantener congruencia.

## Dir raíz
- `/assets`: Contiene Shapefiles, imagenes, y otros recursos.
- `/data_csv`: Contiene CSVs de muestras (100 filas random) de datos de cada tabla del dataset.
- `/docs`: Contiene la documentación del proyecto.
- `/notebooks`: Contiene Jupyter Notebooks utilizados para programar y documentar procesos de ETL y EDA.
- `/src`: El código fuente del proyecto.
- `/tests`: Casos de prueba y scripts de pruebas.

## Dir de Recursos (`/assets`)
- `imagenes/`: Contiene imangenes para uso en README.md.
- Archivos de mapa Shapefile, imagenes, y otros recursos.

## Dir de Documentación (`/docs`)
- `/`: Contiene los archivos "Readme" de cada una de las etapas del proyecto.

## Dir de Notebooks (`/notebooks`)
- `EDA/`: Carpeta con archivos tipo Jupyter Notebooks de análisis exploratorio de datos del datasets original.
- `ETL/`:  Carpeta con archivos tipo Jupyter Notebooks de extracción y transformación de datos del datasets original.
- `conexion_bigquery.ipynb`: Guia para conexion con BigQuery.
- `KPIs_calculos.ipynb`: Calculos de os KPIs rendidos en el dashboard en Looker.

## Dir de Código Fuente (`/src`)
- `Mage/`: Carpeta del programa Mage, que administra la orquestracion de flujos de datos.
- `Reviews_Bot/`: Carpeta del programa Reviews_Bot, interfaz web para el modelo LLM que genera respuestas de reviews.

## Archivos de Configuración
- `requirements.txt`: Lista de librerias Python utilizadas en el proyecto.
