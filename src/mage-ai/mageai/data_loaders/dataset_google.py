from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """

    path_data = '/home/mage/data/raw_parquets'

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


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
