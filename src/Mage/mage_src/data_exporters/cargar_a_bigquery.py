from google.cloud import bigquery

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def cargar_a_bigquery(dfs: dict) -> None:
    """
    """
    #project_id = 'coastal-height-421718'
    dataset = 'Yelp_Google'

    # Create a BigQuery client
    client = bigquery.Client()

    for company, df in dfs.items():
        
        df.reset_index(drop=True, inplace=True)

        nombre_tabla = 'reviews_' + company
        table_ref = client.dataset(dataset).table(nombre_tabla)

        # Set write disposition to 'WRITE_APPEND' to append data
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = 'WRITE_APPEND'
        #job_config.schema = client.get_table(table_ref).schema
        #job_config.autodetect = False
        
        # Load data from your DataFrame
        load_job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        load_job.result()  # Waits for table load to complete

    return dfs