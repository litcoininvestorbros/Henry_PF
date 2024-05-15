# Path de los archivos no-procesados (formato parquet)
"""Funciones que cargan data de datasets Yelp y Google.
"""

from glob import glob
import pickle
import pandas as pd


def cargar_brands() -> dict[list]:
    """Devuele un dict de Darden y sus competidores,
    con una lista de sus repectivas marcas."
    """
    with open('./brands.pickle', 'rb') as f:
        brands = pickle.load(f)
    return brands


def cargar_dataset_google(path_data: str) -> dict[pd.DataFrame]:
    """Devuelve dict de dataframes del dataset
    de Google Maps (un dataframe por tabla).
    """
    # Carga g-sitios.parquet
    df_sitios = pd.read_parquet(f'{path_data}/g-sitios.parquet')

    # Carga g-review.parquet
    # Crear lista de archivos en /data/raw/g-review/
    review_parquets = glob(f'{path_data}/g-review/*')
    # Crear dataframe donde se unen los datos extraidos de parquet
    df_review = pd.DataFrame()
    # Iterar por cada parquet dentro de /data/raw/g-review/
    for p in review_parquets:
        # Leer parquet
        df = pd.read_parquet(p)
        # Unir a df_review
        df_review = pd.concat([df_review, df], ignore_index=True)
    
    return {
        'sitios': df_sitios,
        'review': df_review
}


def cargar_dataset_yelp(path_data: str) -> dict[pd.DataFrame]:
    """Devuelve dict de dataframes del dataset
    de Google Maps (un dataframe por tabla).
    """
    # Carga y-business.parquet
    df_business = pd.read_parquet(f'{path_data}/y-business.parquet')
    # Carga y-checkin.parquet
    df_checkin = pd.read_parquet(f'{path_data}/y-checkin.parquet')
    # Carga y-tip.parquet
    df_tip = pd.read_parquet(f'{path_data}/y-tip.parquet')

    # Carga y-review.parquet
    # Crear lista de archivos en /data/raw/y-review/
    review_parquets = glob(f'{path_data}/y-review/*')
    # Crear dataframe donde se unen los datos extraidos de parquet
    df_review = pd.DataFrame()
    # Iterar por cada parquet dentro de /data/raw/y-review/
    for p in review_parquets:
        # Leer parquet
        df = pd.read_parquet(p)
        # Unir a df_review
        df_review = pd.concat([df_review, df], ignore_index=True)
    
    # Crear lista de archivos en /data/raw/y-user/
    user_parquets = glob(f'{path_data}/y-user/*')
    user_parquets
    # Crear dataframe donde se unen los datos extraidos de parquet
    df_user = pd.DataFrame()
    # Iterar por cada parquet dentro de /data/raw/y-user/
    for p in user_parquets:
        # Leer parquet
        df = pd.read_parquet(p)
        # Unir a df_user
        df_user = pd.concat([df_user, df], ignore_index=True)
    
    return {
        'business': df_business,
        'checkin': df_checkin,
        'tip': df_tip,
        'review': df_review,
        'user': df_user
    }
