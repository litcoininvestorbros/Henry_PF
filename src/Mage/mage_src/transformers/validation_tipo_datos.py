import datetime
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(dfs: dict):
    """
    """
    dfs_output = {}
    for company, df in dfs.items():
        df['date'] = pd.to_datetime(df['date']).dt.date.astype(str)
        df['date'] = df['date'].apply(lambda v: datetime.datetime.strptime(v, "%Y-%m-%d").date())

        ####    TESTING
        df.drop(columns=['date'], inplace=True)
        ####

        dfs_output[company] = df
    
    return dfs_output


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
