from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def cargar_a_bigquery(dfs: dict) -> None:
    """
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Nombres de proyecto y dataset en Google Cloud
    project_id = 'coastal-height-421718'
    dataset = 'Yelp_Google'

    for company, df in dfs.items():
        nombre_tabla = 'reviews_' + company
        table_id = '{project_id}.{dataset}.{nombre_tabla}'
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            table_id,
            if_exists='append'  # Specify resolution policy if table name already exists
        )

    return dfs