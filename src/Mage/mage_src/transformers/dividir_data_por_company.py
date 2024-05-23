if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    """
    df = data
    # Identificar `company` unicos
    company_unicos = df['company'].dropna().unique()

    dfs = {}  # Almacen de resultados del siguiente loop
    # Iterar por cada valor en `company_unicos`, agregandolos como key en `dfs` con
    # valor de un dataframe filtrado por `company`
    for company in company_unicos:
        dfs[company] = df[df_darden_y_comp['company'] == company].drop('company', axis=1)

    return dfs


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
