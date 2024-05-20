## Análisis y manejo de reseñas con herramientas de Machine Learning 

La propuesta de mejora de la imagen del grupo Darden en Yelp, incluye el tratamiento de reseñas. Inicialmente se van a clasificar las reseñas según la calificación en estrellas que tenga cada una de ellas, para luego abordarlas según el siguiente criterio: Las reseñas positivas van a ser respondidas automáticamente por un Bot de respuesta. Las reseñas negativas van a ser analizadas para determinar puntos de mejora y luego serán respondidas de manera manual por personal de Darden. Se anexa a continuación un gráfico que resume el flujo de las reseñas:

<div align="center">
    <img src="../assets/imagenes/flujo_resenias.png" alt="flujo_reseñas" width="700">
</div>

### Reseñas Positivas:

Para generar las respuestas automáticas a las reseñas positivas, después de varias pruebas y una investigación intesiva, se determinó que se podía implementar un modelo lingüistico grande, o "LLM" (Large Language Model) en inglés.  
Estos modelos, desarrollados por las compañías líderes del mercado, ofrecen muchas variantes ajustadas con propósitos específicos "Fine Tune", realizadas por usuarios especializados y disponibles abiertamente para su utilización.  
En nuestro caso se optó por elegir el modelo Mistral-7B como base, y para no trabajar con el modelo completo, debido a que no se necesitan todas sus cualidades y también para reducir requisitos de cómputo, se optó por la versión "mistral-7b-instruct-v0.2.Q5_K_M.gguf", tuneada por el usuario popular "TheBloke", o también "Tom Jobbins" en las redes. La versión "K_M" demanda 5.13GB de disco y 7.63GB de RAM, frente a los más de 15GB de disco y demandas de 30GB a 90GB de RAM, de un modelo Mistral completo, y en este caso, literalmente del autor "very low quality loss".  
La extensión GGUF de los modelos los hace compatibles con la librería "ctransformers" de Python, que es la utilizada en este proyecto.  
Finalmente, para mostrar y testear el modelo, se realizó un despliegue en un servidor propio, utilizando la librería Pynecone.  

### Reseñas Negativas

Para encontrar aspectos problemáticos reseñados negativamente, se partió de un dataset de entrenamiento con más de 2000 reseñas clasificadas con opciones múltiples en una lista predefinida de problemas comunes en la categoría de casas de comidas.  
Haciendo uso de las herramientas de la librería "ScikitLearn" se probaron varias configuraciones y modelos de clasificación múltiple (debido a que una reseña puede incluir más de un aspecto negativo), hasta lograr los resultados deseados.
