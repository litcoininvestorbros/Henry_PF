from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from glob import glob
import pickle
import pandas as pd


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


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
