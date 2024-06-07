
# Descripción y aclaraciones de los cuadernos de ETL y EDA

## ETL

#### ["categorias_a_csv.ipynb"](../notebooks/ETL/categorias_a_csv.ipynb):

En este cuaderno se realizó el recuento de cantidad de negocios en cada categoría. Aquí se notó que la mayor parte de los datos eran sobre casas de comida.

#### ["metadata_google.ipynb"](../notebooks/ETL/metadata_google.ipynb):

En este cuaderno se realiza una inspección general de los nogocios listados en el dataset de Google haciendo foco en restaurants en los estados de nuestro interés.

#### ["reviews_google.ipynb"](../notebooks/ETL/reviews_google.ipynb):

En este cuaderno se aislan las reviews de Google de los estado abarcados por nuestro proyecto.

#### ["transform_datasets_a_parquets.ipynb"](../notebooks/ETL/transform_datasets_a_parquets.ipynb):

En este cuaderno se transforman todos los archivos recibidos en formato JSON a Parquet, con el fin de que ocupen menos espacio, sean más manipulables, y subirlos al data lake de Google Cloud. Por otro lado se generan archivos .csv de muestra de 100 filas, para que los miembros del equipos tengan un primer contacto con los datos sin necesidad de requerir gran potencia de cómputo.

### ["transform_raw_to_clean.ipynb"](../notebooks/ETL/transform_raw_to_clean.ipynb):

En este notebook encontramos la última etapa del proceso de ETL. En él, se desanidan las columnas con datos anidados, y se aplican los filtros que corresponden al alcance del proyecto: Restaurantes dentro de los estados de Delaware, Pensilvania, New Jersey y Florida. Respecto a este criterio, se está creando un producto que puede ser extrapolado a otras áreas, por lo que en un principio se decide trabajar con un sector más acotado hasta obtener el producto final, para luego en caso de que se decida avanzar con el proyecto, se pueda plasmar en todo el territorio.  
Con respecto al área, es oportuno notar que se detectaron valores equivocados en la etiqueta de estado, por lo que el filtro se aplicó a partir de las coordenadas geográficas, haciendo foco en el centro de las áreas metropolitanas de interés (Philadelphia y Tampa), estableciendo un radio de 50km a la redonda, y ubicando todos los locales que se encontraban dentro del sector definido.
Una vez ubicados los negocios del área de influencia seleccionada, se filtró el resto de las tablas con estos negocios.

## EDA

#### ["google_dataset.ipynb"](../notebooks/EDA/google_dataset.ipynb):

En este cuaderno se realiza un análisis exploratorio del dataset de Google. Se encontró que el aporte de reseñas de Google a nuestro proyecto es despreciable, por lo que solo se va a trabajar con las reseñas de Yelp.

#### ["yelp_business.ipynb"](../notebooks/EDA/yelp_business.ipynb):

En este cuaderno se realiza un análisis exploratorio del archivo de "business" de Yelp, haciendo foco en los restaurantes.

### ["yelp_darden_y_comp.ipynb"](../notebooks/EDA/yelp_darden_y_comp.ipynb):

En este cuaderno se realiza un análisis detallado de la cantidad de locales de cada cadena del grupo Darden, y de los grupos que consideramos principales competencias de Darden. Luego se revisa también la cantidad de reseñas de las cadenas analizadas previamente.

#### ["yelp_exploracion_estados.ipynb"](../notebooks/EDA/yelp_exploracion_estados.ipynb):

En este cuaderno se explora principalmente la cantidad de restaurants por estado, para determinar si hay suficientes datos para el alcance elegido en el proyecto. Concluyendo en SÍ.

### ["yelp_general.ipynb"](../notebooks/EDA/yelp_general.ipynb):

En este notebook se realiza el proceso general de EDA. Entre otras cosas, se revisan nulos, columnas innecesarias, datos erróneos, outliyers, realizando diversos gráficos y mapas para tener un panorama completo de los datos proporcionados por la plataforma Yelp.

### ["yelp_review.ipynb"](../notebooks/EDA/yelp_review.ipynb):

En este cuaderno se analiza al detalle el archivo de reseñas de Yelp, haciendo foco en los restaurantes, en los estados de alcance del proyecto, y finalmente en los locales de la cadena Darden.