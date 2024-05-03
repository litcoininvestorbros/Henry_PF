"""Funciones para inicializar base de datos en PostgreSQL
"""

import json
import pandas as pd
from sqlalchemy import create_engine


def cargar_df_a_postgres(df: pd.DataFrame, nombre_tabla: str, uri_db: str, if_exists='replace') -> None:
    """Carga un archivo parquet a una nueva tabla en PostgreSQL,
    si la tabla no exite. Si la tabla existe, el parquet se anexa.
    """
    # Crear un motor de base de datos
    engine = create_engine(uri_db)
    # Anexar el dataframe a la tabla SQL
    df.to_sql(nombre_tabla, engine, if_exists=if_exists, index=False)

    # Cerrar la conexión
    engine.dispose()


def transforms_compatibilidad_postgres(df: pd.DataFrame, nom_archivo: str) -> pd.DataFrame:
    """transforms_de_compatibilidad
    """
    if nom_archivo == 'y_business':
        df['attributes'] = df['attributes'].apply(json.dumps)
        df['categories'] = df['categories'].apply(lambda x: str(x).split(',')).apply(json.dumps)
        df['hours'] = df['hours'].apply(json.dumps)

    elif nom_archivo == 'y_checkin':
        df.set_index('business_id', inplace=True)
        df['date'] = df['date'].str.split(',')
        df = df.explode('date')
        df['date'] = pd.to_datetime(df['date'], format='mixed')
        df.reset_index(inplace=True)

    elif nom_archivo == 'y_review':
        pass

    elif nom_archivo == 'y_user':
        df['elite'] = df['elite'].apply(lambda x: str(x).split(',')).apply(lambda x: json.dumps(x) if x[0] else None)
        df['friends'] = df['friends'].apply(lambda x: str(x).split(',')).apply(lambda x: json.dumps(x) if x[0] != "None" else None)
        df.reset_index(drop=True, inplace=True)

    elif nom_archivo == 'y_tip':
        pass

    elif nom_archivo == 'g_sitios':
        df['category'] = df['category'].apply(lambda x: json.dumps(x.tolist()) if x is not None else None)
        df['hours'] =  df['hours'].apply((lambda x: json.dumps(dict(x.tolist())) if x is not None else None))
        df['relative_results'] = df['relative_results'].apply(lambda x: json.dumps(x.tolist()) if x is not None else None)
        df.drop('MISC', axis=1, inplace=True)
        df.drop('url', axis=1, inplace=True)

    elif nom_archivo == 'g_review':
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        df['rating'] = df['rating'].astype('int16')
        df['text'] = df['text'].apply(lambda x: x.replace('\x00', ' ') if isinstance(x, str) else x)
        df.drop('pics', axis=1, inplace=True)
        df.drop('resp', axis=1, inplace=True)
        
    return df