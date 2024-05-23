from google.cloud import bigquery

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    """
    client = bigquery.Client()

    merge_statement = """
    MERGE `your_project.your_dataset.your_target_table` T
    USING `your_project.your_dataset.your_temp_table` S
    ON T.review_id = S.review_id
    WHEN MATCHED THEN
    UPDATE SET T.column1 = S.column1, T.column2 = S.column2
    WHEN NOT MATCHED THEN
    INSERT (review_id, column1, column2) VALUES(review_id, column1, column2)
    """

    # Execute the MERGE statement
    query_job = client.query(merge_statement)
    query_job.result()  # Wait for the job to complete

