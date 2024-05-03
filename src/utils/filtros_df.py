"""Funciones para filtros complejos de dataframes.
"""

import pandas as pd


# Dict de regiones/areas metro en USA
areas_metro = {
    'NY': [
        'New York, NY', 'Newark, NJ', 'Jersey City, NJ',
        'Yonkers, NY', 'Paterson, NJ', 'Elizabeth, NJ',
        'Stamford, CT', 'Edison, NJ', 'New Rochelle, NY',
        'Mount Vernon, NY', 'White Plains, NY', 'Hempstead, NY',
        'Union City, NJ', 'Wayne, NJ', 'North Hempstead, NY'
    ],
    'LA': [
        'Los Angeles, CA', 'Long Beach, CA', 'Anaheim, CA',
        'Santa Ana, CA', 'Irvine, CA', 'Glendale, CA',
        'Huntington Beach, CA', 'Santa Clarita, CA', 'Garden Grove, CA',
        'Lancaster, CA', 'Palmdale, CA', 'Pomona, CA',
        'Torrance, CA', 'Pasadena, CA', 'Orange, CA'
    ],
    'CHI': [
        'Chicago, IL', 'Aurora, IL', 'Naperville, IL',
        'Joliet, IL', 'Elgin, IL', 'Kenosha, WI',
        'Waukegan, IL', 'Cicero, IL', 'Hammond, IN',
        'Gary, IN', 'Arlington Heights, IL', 'Evanston, IL',
        'Schaumburg, IL', 'Bolingbrook, IL', 'Palatine, IL'
    ],
    'TX': [
        'Dallas, TX', 'Fort Worth, TX', 'Arlington, TX',
        'Plano, TX', 'Irving, TX', 'Garland, TX',
        'Grand Prairie, TX', 'McKinney, TX', 'Frisco, TX',
        'Mesquite, TX', 'Carrollton, TX', 'Denton, TX',
        'Richardson, TX', 'Lewisville, TX', 'Allen, TX'
    ],
    'FL': [
        'Tampa, TX', 'Fort Worth, TX', 'Arlington, TX',
        'Plano, TX', 'Irving, TX', 'Garland, TX',
        'Grand Prairie, TX', 'McKinney, TX', 'Frisco, TX',
        'Mesquite, TX', 'Carrollton, TX', 'Denton, TX',
        'Richardson, TX', 'Lewisville, TX', 'Allen, TX'
    ]
}


def filtrar_por_region(df: pd.DataFrame, nombre_dataset: str, filtra_region: str | list) -> pd.DataFrame:
    """`df`: dataframe del dataset Google, tabla `sitios`, o dataset Yelp, tabla `business` 
    `nombre_dataset`: nombre del dataset del dataframe de entrada (valores aceptados: 'google', 'g', 'yelp', 'y')
    `filtra_region`: string o lista de regiones (valores aceptados: 'NY', 'LA', 'CHI', 'TX')
    """
    if nombre_dataset not in ['google', 'g', 'yelp', 'y']:
        raise ValueError(f'Argumento invalido -> {nombre_dataset=}, valores aceptados: `google`, `g`, `yelp`, `y`')
    
    if not type(filtra_region) == list:
        filtra_region = [filtra_region.upper()]
    else:
        filtra_region = [str(s).upper() for s in filtra_region]

    listas_ciudades = [areas_metro[k] for k in filtra_region if k in areas_metro]
    ciudades = [c for sublista in listas_ciudades for c in sublista]

    df_out = pd.DataFrame()

    if nombre_dataset in ['google', 'g']:
        pass
    
    elif nombre_dataset in ['yelp', 'y']:
        for c in ciudades:
            ciudad, estado = c.split(',')
            estado.replace(' ','')
            
            df_filtro =  df[(df['city'] == ciudad)]# & (df['state'] == estado)]
            df_out = pd.concat([df_out, df_filtro], ignore_index=True)

    return df_out
