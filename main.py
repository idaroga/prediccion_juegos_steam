from fastapi import FastAPI
import pandas as pd


# Lectura de CSV en un df
ruta_1 = "eda_userdata.csv"
df_userdata = pd.read_csv(ruta_1)

# Lectura de CSV en un df
ruta_2 = "eda_countreviews.csv"
df_countreviews = pd.read_csv(ruta_2)

# Lectura de CSV en un df
ruta_3 = "eda_genre.csv"
df_genre = pd.read_csv(ruta_3)

# Lectura de CSV en un df
ruta_4 = "eda_userforgenre.csv"
df_userforgenre = pd.read_csv(ruta_4)

# Lectura de CSV en un df
ruta_5 = "eda_developer.csv"
df_developer = pd.read_csv(ruta_5)

# Lectura de CSV en un df
ruta_6 = "eda_sentiment_analysis.csv"
df_sentiment_analysis = pd.read_csv(ruta_6)

# code here:


app = FastAPI()


@app.get("/")
def hola_mundo():
    return {"hola, link a fastAPI: https://pi-mlops-steam-ivan.onrender.com/docs"}


@app.get("/username/{user_id}")
def userdata (user_id:str):
    '''
    Función que recibe de entrada el ID de un usuario y devuelve:
    - Cantidad total de dinero que ha gastado en items
    - Cantidad total de items que posee
    - Porcentaje de items que recomienda respecto al total de items que posee.
    '''

    user_id = str(user_id)
    user_id = user_id.strip()

    df_filtrado = df_userdata[df_userdata["user_id"] == user_id]
    mi_dict = df_filtrado.to_dict(orient='records')

    return mi_dict[0]


@app.get("/countreviews/{desde}, {hasta}")
def countreviews (desde:str, hasta:str):
    '''
    Función que recibe dos fechas de entrada en formato YYYY-MM-DD y devuelve:
    - Cantidad de usuarios que realizaron reviews entre las fechas dadas
    - Porcentaje de items que se recomiendan de acuerdo a todas las reviews que se realizaron entre esas fechas.
    '''

    desde = str(desde)
    desde = desde.strip().replace("-","")
    desde = int(desde)
    
    hasta = str(hasta)
    hasta = hasta.strip().replace("-","")
    hasta = int(hasta)

    df_filtrado = df_countreviews[(df_countreviews["posted_date_num"] >= desde) &
                                    (df_countreviews["posted_date_num"] <= hasta)]

    user_count = df_filtrado["user_id"].nunique()
    recommend_count = df_filtrado["recommend"].count()
    recommend_sum = df_filtrado["recommend"].sum()
    recommend_percent = round(recommend_sum / recommend_count *100, 2)

    mi_dict = {"user_count": user_count, 
                "recommend_percent": recommend_percent
                }

    return mi_dict


@app.get("/genre/{genre}")
def genre(genre:str):
    '''
    Función que recibe de entrada un género de juego y devuelve:
    - Lugar que ocupa dicho género en un ranking de todos los géneros de acuerdo al tiempo total de juego para cada género.
    
    Nota: El género con mayor cantidad de tiempo jugado ocupará la posición #1 del ranking
    '''

    look_genre = genre.lower().replace(" ", "")

    df_filtrado = df_genre[["Genre", "Ranking"]][df_genre["look_genre"] == look_genre]
    mi_dict = df_filtrado.to_dict(orient='records')

    return mi_dict[0]


@app.get("/userforgenre/{genre}")
def userforgenre(genre:str):
    '''
    Función que recibe de entrada un género de juego y devuelve:
    - Lista de 5 usuarios con mayor cantidad de horas de juego para dicho género.
    - URL de cada usuario
    
    Nota: El usuario con mayor cantidad de tiempo jugado ocupará la posición #1 del ranking
    '''

    look_genre = genre.lower().replace(" ", "")

    df_filtrado = df_userforgenre[["ranking", "user_id", "user_url"]][df_userforgenre["look_genre"] == look_genre]
    mi_list = df_filtrado.to_dict(orient='records')

    claves = []
    for indice in range (0,5):
        valor = "Ranking_" + str(indice + 1)
        claves.append(valor)

    mi_dict = {}

    for indice, clave in enumerate(claves):
        user_id = df_filtrado['user_id'].iloc[indice]
        url_user = df_filtrado["user_url"].iloc[indice]
        registro = "user_id: " + user_id + " // url_user: " + url_user
        mi_dict[clave] = registro

    return mi_dict


@app.get("/developer/{developer}")
def developer(developer:str):
    '''
    Función que recibe de entrada el nombre de un desarrollador y devuelve:
    - Lista de años en los que el desarrollador hizo lanzamiento de items
    - Cantidad de items por año
    - Porcentaje de items free respecto al total de items lanzados ese el año
    '''

    look_developer = developer.lower().replace(" ", "")

    df_filtrado = df_developer[["release_year", "items_count", "free_percent"]][df_developer["look_developer"] == look_developer]
    df_filtrado = df_filtrado.reset_index()

    lista_claves = df_filtrado['release_year'].tolist()
    mi_dict = {}

    for indice, clave in enumerate(lista_claves):
        items_count = df_filtrado['items_count'].iloc[indice]
        free_percent = df_filtrado["free_percent"].iloc[indice]
        registro = "items_count: " + str(items_count) + " // free_percent: " + str(free_percent)
        mi_dict[clave] = registro

    return mi_dict


@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year:str):
    '''
    Función que recibe de entrada un año y devuelve:
    - Listado de categorias basadas en el analisis de sentimiento de las reseñas realizadas en ese año de los items
    - Cantidad total de reseñas para cada categoría de analisis de sentimiento
    '''
    year = float(year)

    df_filtrado = df_sentiment_analysis[["sentiment_label", "count"]][df_sentiment_analysis["release_year"] == year]
    df_filtrado = df_filtrado.groupby(["sentiment_label"])["count"].sum().reset_index()
    mi_dict = df_filtrado.to_dict(orient='records')

    lista_claves = df_filtrado['sentiment_label'].tolist()
    mi_dict = {}

    for indice, clave in enumerate(lista_claves):
        mi_dict[clave] = str(df_filtrado["count"].iloc[indice])

    return mi_dict