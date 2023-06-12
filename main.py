import pandas as pd
import numpy as np
from etl import movies_data, credits
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello Worlds"

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    months = {
        'enero': 'January',
        'febrero': 'February',
        'marzo': 'March',
        'abril': 'April',
        'mayo': 'May',
        'junio': 'June',
        'julio': 'July',
        'agosto': 'August',
        'septiembre': 'September',
        'octubre': 'October',
        'noviembre': 'November',
        'diciembre': 'December'
    }
    
    mes = mes.lower().strip()

    month_in_English = months.get(mes, None)
    if month_in_English is None:
        return {'mes':mes, 'cantidad': 'El nombre del mes ingresado no es valido'}
    else:
        filter_per_month = movies_data['release_date'].dt.month_name() == month_in_English
        movie_counter = filter_per_month.sum()
        return {'mes':mes, 'cantidad':int(movie_counter)}

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia historicamente'''
    days = {
        'lunes': 'Monday',
        'martes': 'Tuesday',
        'miercoles': 'Wednesday',
        'jueves': 'Thursday',
        'viernes': 'Friday',
        'sabado': 'Saturday',
        'domingo': 'Sunday'
    }
    
    dia = dia.lower().strip()

    day_in_English = days.get(dia, None)
    if day_in_English is None:
        return {'dia':dia, 'cantidad': 'El nombre del dia ingresado no es valido'}
    else:
        filter_per_day = movies_data['release_date'].dt.day_name() == day_in_English
        movie_counter = filter_per_day.sum()
        return {'dia':dia, 'cantidad':int(movie_counter)}

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score'''
    movie = movies_data[movies_data['title'] == titulo]
    if movie.empty:
        return {'msg': 'No se ha encontrado ninguna pelicula que coincida con el titulo ingresado'}
    else:
        return {'titulo':titulo, 
                'anio':int(movie['release_year'].values[0]), 
                'popularidad':float(movie['popularity'].values[0])}

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    '''Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.'''
    movie = movies_data[movies_data['title'] == titulo]
    if movie.empty:
        return {'msg': 'No se ha encontrado ninguna pelicula que coincida con el titulo ingresado'}
    elif movie['vote_count'].values[0] < 2000:
        return {'msg': 'La pelicula ingresada no cuenta con al menos 2000 valoraciones'}
    else:
        return {'titulo':titulo, 
                'anio':int(movie['release_year'].values[0]), 
                'voto_total':int(movie['vote_count'].values[0]), 
                'voto_promedio':float(movie['vote_average'].values[0])}

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno'''
    actor_movies = credits[credits['cast'].apply(lambda x: any(dict['name'] == nombre_actor for dict in x))]
    if actor_movies.empty:
        return {'msg': 'No se ha encontrado el actor ingresado'}
    else:
        actor_movie_ids = actor_movies['id']
        actor_movies_data = movies_data[movies_data['id'].isin(actor_movie_ids)]
        num_movies_participated = actor_movies_data.shape[0]
        actor_total_return = actor_movies_data['return'].sum()
        actor_average_return = actor_total_return / num_movies_participated if num_movies_participated > 0 else 0
        return {'actor':nombre_actor, 
                'cantidad_filmaciones':int(num_movies_participated), 
                'retorno_total':float(actor_total_return), 
                'retorno_promedio':float(actor_average_return)}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.'''
    director_movies = credits[credits['crew'].apply(lambda x: any(dict['name'] == nombre_director and dict['job'] == 'Director' for dict in x))]
    
    if director_movies.empty:
        return {'msg': 'No se ha encontrado el director ingresado'}
    else:
        director_movie_ids = director_movies['id']
        director_movies_data = movies_data[movies_data['id'].isin(director_movie_ids)]

        director_movies_info = []
        for _, movie in director_movies_data.iterrows():
            movie_info = {
                'titulo': str(movie['title']),
                'fecha_lanzamiento': str(movie['release_date'].date()),
                'retorno_pelicula': float(movie['return']),
                'budget_pelicula': int(movie['budget']),
                'revenue_pelicula': int(movie['revenue'])
            }
            director_movies_info.append(movie_info)

        return {
                'director': nombre_director,
                'retorno_total_director': int(director_movies_data['return'].sum()),
                'peliculas': director_movies_info
                }