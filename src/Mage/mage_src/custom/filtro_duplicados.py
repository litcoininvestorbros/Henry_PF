from google.cloud import bigquery

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


class PipelineTerminationException(Exception):
    pass


@custom
def filtrar_reviews_duplicados(dfs: dict):
    """
    """
    # Nombres de proyecto y dataset en Google Cloud
    project_id = 'coastal-height-421718'
    dataset = 'Yelp_Google'
    #nombre_tabla = ''
    columna = 'review_id'

    client = bigquery.Client()

    dfs_output = {}
    for company, df in dfs.items():
        nombre_tabla = 'reviews_' + company
        # Definir query
        query = f"""
        SELECT {columna}
        FROM `{project_id}.{dataset}.{nombre_tabla}`
        """
        query_job = client.query(query)
        # Get the results as a list
        review_ids = [fila[columna] for fila in query_job.result()]

        
        # Usar lista para validar si datos son duplicados
        df['es_duplicado'] = df['review_id'].isin(review_ids)
        df = df[df['es_duplicado'] == False]
        df.drop(columns=['es_duplicado'], inplace=True)

        # Continuar loop si no hay datos nuevos (no-duplicados)
        if not df.shape[0]:
            continue
        
        # Agregar columna a Darden, usado para respuestas de reviews
        if company == 'darden':
            df['text_reply'] = ''

        # Agregar dataframe a dict de return
        dfs_output[company] = df
    
    if not dfs_output:
        raise PipelineTerminationException(
            "Todo review entrante via API es un duplicado."
        )

    return dfs_output


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
