# Delphi

![vista frontal del cine](https://github.com/HolyGrace/Delphi/blob/master/src/joel-muniz-IkSjU7Ij2xk-unsplash.jpg)

**Delphi** es un sistema de recomendación de películas que utiliza técnicas de filtrado colaborativo para recomendar películas a los usuarios 🎬🍿. También proporciona funciones de consulta a los conjuntos de datos utilizados en el sistema.

## Conjuntos de Datos Disponibles
1. ``movies.csv``: Este archivo contiene información sobre las películas disponibles en el sistema de recomendación 🎟️. Incluye detalles como el título, género y descripción de cada película.

2. ``credits.csv``: Este archivo contiene información sobre los créditos de las películas, incluyendo los actores y directores  involucrados en cada una 🧙🏻‍♂️🧛🏻‍♂️🧝🏻‍♀️.

## Funciones de Consulta Disponible a los Conjuntos de Datos
El sistema de recomendación ofrece las siguientes funciones de consulta a los conjuntos de datos:

1. ``cantidad_filmaciones_mes(mes)``: Esta función devuelve la cantidad de filmaciones realizadas en un mes específico. El parámetro ``mes`` debe ser proporcionado en formato texto (por ejemplo, enero).

2. ``cantidad_filmaciones_dia(dia)``: Esta función devuelve la cantidad de filmaciones realizadas en un día específico. El parámetro ``dia`` debe ser proporcionado en formato texto (por ejemplo, domingo).

3. ``score_titulo(titulo_de_la_filmación)``: Esta función devuelve el puntaje o calificación de una película específica, identificada por su título.

4. ``votos_titulo(titulo_de_la_filmación)``: Esta función devuelve la cantidad de votos recibidos por una película específica, identificada por su título.

5. ``get_actor(nombre_actor)``: Esta función devuelve información detallada sobre un actor específico, incluyendo las películas en las que ha participado. El parámetro ``nombre_actor`` debe ser proporcionado para obtener información sobre ese actor en particular.

6. ``get_director(nombre_director)``: Esta función devuelve información detallada sobre un director específico, incluyendo las películas que ha dirigido. El parámetro ``nombre_director`` debe ser proporcionado para obtener información sobre ese director en particular.

7. ``recomendacion(titulo)``: Esta función recomienda películas relacionadas con un título específico. Utiliza técnicas de filtrado colaborativo para sugerir películas que podrían interesar al usuario. El parámetro ``titulo`` debe ser proporcionado para obtener recomendaciones basadas en esa película.

## Requisitos de Instalación
Para utilizar el sistema de recomendación y las funciones de consulta, se requiere la instalación de las siguientes dependencias:

- Python 3.x
- Pandas
- Numpy
- Scikit-learn
- FastAPI
- Uvicorn

## Uso
1. Clone este repositorio en su máquina local.

2. Asegúrese de tener Python 3.x instalado.

3. Instale las dependencias necesarias ubicandose en la ruta donde se encuentra el archivo ``requirements.txt`` y ejecutando el siguiente comando en la terminal:

    ```
    $ pip install -r requirements.txt
    ```

4. Utilice las funciones de consulta provistas para obtener información detallada sobre las películas, explorar datos relacionados con las filmaciones, obtener puntajes y votos de películas específicas, buscar información sobre actores y directores, y recibir recomendaciones personalizadas.

Esperamos que este sistema de recomendación de películas y las funciones de consulta a los conjuntos de datos sean útiles para explorar y descubrir películas según las preferencias y calificaciones de los usuarios. ¡Disfruta de tus películas recomendadas! ✨🌠