# El Camino de los Datos

## Overview

Este documento describe el camino que recorren, y los precesos que reciben los datos, desde su obtención hasta su disposición final en el warehouse, para ser utilizados.

### Esquema Global

A continuación se muestra el esquema global del pipeline.

<div align="center">
    <img src="../assets/imagenes/pipeline.jpg" alt="flujo_reseñas" width="700">
</div>

Como se puede apreciar, los datos se reciben desde dos fuentes distintas, un dataset inicial para analizar la factibilidad y alcances del proyecto, y un consumo de datos desde la API de Yelp.

## Camino del Dataset inicial

Los archivos fueron recibidos en formato Parquet y Json, desde un Drive compartido.  

<div align="center">
    <img src="../assets/imagenes/archivos_yelp.jpg" alt="flujo_reseñas" width="300">
</div>

Estos archivos son tomados desde Google Cloud por Cloud Functions, y mediante código Python y la librería Pandas, son procesados y enviados a BigQuery.

<div align="center">
    <img src="../assets/imagenes/cloud_function.jpg" alt="flujo_reseñas" width="300">
</div>

## Pipeline dinámico actual

Actualmente el camino de los datos comienza con su obtención, mediante el consumo de la API de la plataforma YELP. 

<div align="center">
    <img src="../assets/imagenes/flujo_api.png" alt="flujo_reseñas" width="500">
</div>

La gestión del flujo automatizado de trabajo, que comprende la ejecución del script de consumo del API, el procesado de los datos, la verificación de que no haya reseñas que ya hayan sido recibidas, y el envío de las reseñas nuevas a BigQuery, son orquestados por Mage.Ai.

<div align="center">
    <img src="../assets/imagenes/flujo_mage.png" alt="flujo_reseñas" width="600">
</div>

### BigQuery

Finalmente, el lugar al que llegan todos los archivos, es BigQuery. Dentro de la plataforma se encuentran todas las tablas iniciales, y las tablas originadas para los distintos procesos de visualización y análisis.

<div align="center">
    <img src="../assets/imagenes/big_query.jpg" alt="flujo_reseñas" width="300">
</div>