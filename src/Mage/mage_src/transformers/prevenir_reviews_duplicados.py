from google.cloud import bigquery

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    """
    dfs_input: dict = data

    # Nombres de proyecto y dataset en Google Cloud
    project_id = 'coastal-height-421718'
    dataset = 'Yelp_Google'

    # Instanciar objeto cliente
    client = bigquery.Client()
    """
    dfs = {}
    for company, df in dfs_input.items():


        tabla = 'reviews_' + company
        # Definir query
        sql = f"""
        SELECT review_id
        FROM `{project_id}.{dataset}.{tabla}`
        """

        df_review_id = client.query(sql).to_dataframe()

    
    return dfs"""


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
