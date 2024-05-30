from pprint import pformat
from requests import post
from mage_ai.data_preparation.shared.secrets import get_secret_value

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(dfs: dict) -> bool:
    """
    """
    url = get_secret_value('DISCORD_WEBHOOK')

    lista_msg = ["Reporte de {reviews_id} cargados a BQ:"]
    for company, df in dfs.items():
        lista_msg.append(f"{company.title()}: {df['review_id'].tolist()}")

    content = pformat(lista_msg)
    try:
        post(url, json={'username':'Mage', 'content':content})
        return True
    except Exception as e:
        print(str(e))
        return False


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
