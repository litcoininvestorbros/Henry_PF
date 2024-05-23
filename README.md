<div align="center">
    <img src="assets/imagenes/logo.jpeg" alt="wink" width="200" height="150">
</div>

## Descripción del Proyecto

Este proyecto se enfoca en el analisis exploratorio de datos para la cadena de restaurantes Darden Continuing Operations, donde analizaremos su restaurante  y por medio de un analisis de la informacion y con una propuesta de trabajo definiendo Kpi's buscaremos la manera de mejorar sus calificaciones en las plataformas de recomendaciones como Google y Yelp.

## Descripción del Conjunto de Datos

El conjunto de datos utilizado en este análisis contiene información sobre comentarios que los usuarios de google dejan sobre los establecimientos a los que la app de Google_Maps evidencia que estuvieron, si estos usuarios dejan sus calificaciones y comentarios, tambien existe una metadata la cual contiene toda la informacion acerca de los establecimientos, la cual nos fue util para identificar a que establecimiento hacia referencia el usuario.

## Objetivo

Potenciar la visibilidad y reputación de las marcas del grupo empresarial Darden en la región de Filadelfia y sus alrededores a través de la plataforma Yelp.

# Equipo de trabajo
<h1 align="center">Data Engineering</h1>
<div align="center">
  <div style="display: inline-block; margin: 20px;">
    <img src="assets/imagenes/Felix.jpeg" alt="Foto de Persona 1" style="border-radius: 50%; width: 150px; height: 150px;">
    <h3>Felix Santana</h3>
  </div>
  <div style="display: inline-block; margin: 20px;">
    <img src="assets/imagenes/Jonathan.jpeg" alt="Foto de Persona 1" style="border-radius: 50%; width: 150px; height: 150px;">
    <h3>Jonathan Gutiérrez</h3>
  </div>
</div>
<h1 align="center">Data Analytics</h1>
<div align="center">
  <div style="display: inline-block; margin: 20px;">
    <img src="assets/imagenes/Catalina.jpeg" alt="Foto de Persona 1" style="border-radius: 50%; width: 150px; height: 150px;">
    <h3>Catalina Castelblanco</h3>
  </div>
  <div style="display: inline-block; margin: 20px;">
    <img src="assets/imagenes/Andrew.jpeg" alt="Foto de Persona 1" style="border-radius: 50%; width: 150px; height: 150px;">
    <h3>Andres Mozo</h3>
  </div>
</div>
<h1 align="center">Machine Learning</h1>
<div align="center">
  <div style="display: inline-block; margin: 20px;">
    <img src="assets/imagenes/Facundo.jpeg" alt="Foto de Persona 1" style="border-radius: 50%; width: 150px; height: 150px;">
    <h3>Facundo Sagle</h3>
  </div>
  <div style="display: inline-block; margin: 20px;">
    <img src="assets/imagenes/Marcelo.jpeg" alt="Foto de Persona 1" style="border-radius: 50%; width: 150px; height: 150px;">
    <h3>Marcelo Trinkard</h3>
  </div>  
</div>


## Plan de trabajo

Por medio de la metodologia SCRUM nos organizamos en equipo repartiendo el trabajo de la siguiente manera.

Para diagramar y organizar las tareas a realizar, elaboramos un diagrama de Gantt, en donde se indica el responsable mediante el color de la barra, si tiene a cargo un sector o un conjunto de sector el color será violeta, indicándose que sectores están involucrados, por otra parte, si está a cargo de una única persona en este grafico podemos identificar quien es quien debe realizarla. La extensión y ubicación de la barra indica el periodo de tiempo destinado para esta tarea. 

# Sprint 1
Como se observa, el primer sprint fue destinado principalmente a poner en marcha el proyecto y hacer un análisis preliminar de los datos y las tecnologías a utilizar.


<div style="text-align: center;">
    <img src="assets/imagenes/sprint1.png" alt="wink" >
</div>

# Sprint 2
En el segundo sprint los roles van a ser fundamentales, ya que a diferencia del primero que era más general, ahora cada sector tendrá tareas más específicas y relacionadas al rol definido. Sin embargo, al ser el objetivo principal de este sprint finalizar la infraestructura del proyecto, debe tratarse de forma prioritaria y los demás sectores deben  brindar soporte de ser necesario.

<div style="text-align: center;">
    <img src="assets/imagenes/sprint2.png" alt="wink" >
</div>

# Sprint 3

En el tercer sprint se busca tener los modelos de ML y el dashboard listo en la primera semana para que en la segunda semana se pueda hacer un correcto storytelling y una presentación más elaborada que las anteriores.

<div style="text-align: center;">
    <img src="assets/imagenes/sprint3.png" alt="wink" >
</div>

## Flujo de datos

<div style="text-align: center;">
    <img src="assets/imagenes/pipeline.jpg" alt="wink" >
</div>

## Analisis de los datos
- [`EDA_preliminar_Google.ipynb`](notebooks/eda_google.ipynb)
: Jupyter Notebook que contiene el código y la narrativa del análisis exploratorio de datos en el archivo de reviws suministrado por Google.
- [`EDA_preliminar_YELP.ipynb`](notebooks/eda_yelp.ipynb)
: Jupyter Notebook que contiene el código y la narrativa del análisis exploratorio de datos de los archivos de YELP

## Tecnologias Utilizadas

<a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" style="border-radius: 80%; border: 1px solid #3776AB;">
</a>
<a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" style="border-radius: 50%; border: 1px solid #150458;">
</a>
<a href="https://matplotlib.org/">
    <img src="https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib" style="border-radius: 50%; border: 1px solid #3776AB;">
</a>
<a href="https://seaborn.pydata.org/">
    <img src="https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn" style="border-radius: 50%; border: 1px solid #3776AB;">
</a>
<a href="https://code.visualstudio.com/">
    <img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="Visual Studio Code" style="border-radius: 50 %; border: 1px solid #007ACC;">
</a>
<a href="https://cloud.google.com/">
    <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud" style="border-radius: 50%; border: 1px solid #4285F4;">
</a>
<a href="https://cloud.google.com/bigquery/">
    <img src="https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="BigQuery" style="border-radius: 50%; border: 1px solid #4285F4;">
</a>
<a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" style="border-radius: 50%; border: 1px solid #2496ED;">
</a>
<a href="https://cloud.google.com/ai-platform/">
    <img src="https://img.shields.io/badge/ML_Engine-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="ML Engine" style="border-radius: 50%; border: 1px solid #4285F4;">
</a>
<a href="https://magefile.org/">
    <img src="https://img.shields.io/badge/Mage-00ADD8?style=for-the-badge&logoColor=white" alt="Mage" style="border-radius: 50%; border: 1px solid #00ADD8;">
</a>
<a href="https://www.novipro.com/">
    <img src="https://img.shields.io/badge/Novi_Pro-006DB9?style=for-the-badge&logoColor=white" alt="Novi Pro" style="border-radius: 50%; border: 1px solid #006DB9;">
</a>
<a href="https://powerbi.microsoft.com/">
    <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=microsoft-power-bi&logoColor=white" alt="Power BI" style="border-radius: 50%; border: 1px solid #F2C811;">
</a>
<a href="https://trello.com/">
    <img src="https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white" alt="Trello" style="border-radius: 50%; border: 1px solid #0052CC;">
</a>
<a href="https://www.canva.com/">
    <img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white" alt="Canva" style="border-radius: 50%; border: 1px solid #00C4CC;">
</a>
<a href="https://github.com/">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" style="border-radius: 50%; border: 1px solid #181717;">
</a>

