"""Funciones que almacenan objetos (list, dict) en disco, en formato `pickle`. 
   Estos pickles aportan al uso eficientes de recursos de nube (Google Cloud),
   minimizado los queries que involucran datos estáticos.
"""

import pickle
from google.cloud import bigquery
from rapidfuzz import process, fuzz


def crear_brands_pickle() -> list:
    """Crea dos objetos para archivar como pickles:
    1) Un dict de toda marca/brand, correspondientes a Darden y sus competidores.
    2) Una lista flat de todas las marcas/brands en el dict previo.
    Devuelve un tuple con ambos objetos creados.
    """
    # Diccionario de marcas de Darden y competidores
    brands_por_compania = {
        # Darden brands
        'darden': [
            "Olive Garden Italian Restaurant",
            "Olive Garden",
            "LongHorn Steakhouse",
            "Cheddar's Scratch Kitchen",
            "Yard House",
            "The Capital Grille",
            "Seasons 52",
            "Bahama Breeze",
            "Eddie V's",
            "Eddie V's Prime Seafood",
            "Ruth's Chris Steak House"
        ],
        # Bloomin brands
        'bloomin': [
            "Outback Steakhouse",
            "Carrabba's Italian Grill",
            "Bonefish Grill",
            "Fleming's Prime Steakhouse & Wine Bar",
            "Aussie Grill by Outback",
            "Aussie Grill - Brandon",
            "Aussie Grill - Clearwater",
            "Aussie Grill - ",
            "Aussie Grill"
        ],
        # Brinker brands
        'brinker': [
            "Chili's",
            "Chili's Grill & Bar",
            "Maggiano's Little Italy",
            "It's Just Wings"
        ],
        # Texas Roadhouse brands
        'texasroadhouse': [
            "Texas Roadhouse",
            "Bubba's 33"
        ]
    }
    with open('./data/brands_por_compania.pickle', 'wb') as f:
        pickle.dump(brands_por_compania, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    lista_nombres_brands = [brand for lista in brands_por_compania.values() for brand in lista]
    with open('./data/brands_darden_y_comp.pickle', 'wb') as f:
        pickle.dump(lista_nombres_brands, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    return (brands_por_compania, lista_nombres_brands)


def crear_df_darden_y_comp_pickle(brands_por_compania, lista_nombres_brands) -> None:
    """Crea un archivo pickle de un DataFrame de datos provenientes de
    la tabla `y_business` en BigQuery. Los datos incluidos en la lista son unicamente
    los que corresponden a Darden y sus competidores (basandose en la lista de entrada `filtro_name`).
    Devuelve el DataFrame creado.
    """
    # Nombres de proyecto, dataset y tabla en Google Cloud
    project_id = 'coastal-height-421718'
    dataset = 'Yelp_Google'
    tabla = 'y_business'

    # Instanciar objeto cliente
    client = bigquery.Client()

    # Definir query
    sql = f"""
    SELECT name, business_id, city, state, postal_code, coordinates
    FROM `{project_id}.{dataset}.{tabla}`
    """

    # Ejecutar query y almacenar resultado en un DataFrame
    df = client.query(sql).to_dataframe()


    # Funcion que implementa busqueda 'fuzzy' en textos.
    # Se bucan las marcas/brands por nombre. Por la variacion en
    # nombres en el dataset, se implementa una busqueda fuzzy
    # para asegurar que se filtren los `business_id` esperados.
    def fuzzy_match(x, match_to, threshold=90):
        match, score, _ = process.extractOne(x, match_to, scorer=fuzz.WRatio)
        return match if score >= threshold else None
    
    # Aplicar fuzzy matching para Darden
    df['name_match'] = df['name'].apply(fuzzy_match, match_to=lista_nombres_brands)
    # Filtrar nulos (donde nulo representa no-match)
    df = df[df['name_match'].notnull()]
    # Descartar columna de utilidad filtro
    df.drop(columns=['name_match'], inplace=True)

    # Agregar columna con nombre de compañia dueño de las marcas/brands
    # Invertir el dict `brands_por_compania` para crear un mapeo de `name` nombre de compañia
    dict_invertido = {string: key for key, lista in brands_por_compania.items() for string in lista}
    # Mapeo de nombre de marcas `name` a su compañia dueño
    df['company'] = df['name'].map(dict_invertido)

    # Almacenar lista filtrada en disco
    df.to_pickle('./data/df_darden_y_comp.pickle')



if __name__ == '__main__':
    # Llamar las dos funciones declaradas en este archivo, subsecuentemente,
    # donde `crear_df_darden_y_comp_pickle()` depende del output de `crear_brands_pickle()`
    crear_df_darden_y_comp_pickle(*crear_brands_pickle())
