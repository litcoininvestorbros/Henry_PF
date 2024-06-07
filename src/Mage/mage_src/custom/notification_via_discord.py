from time import sleep
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

    lista_msg = ["__Reporte de Reseñas Nuevas__"]
    for company, df in dfs.items():
        lista_msg.append(f"\n**{company.title()}**")
        for item in df['review_id'].tolist():
            lista_msg.append(item)

    content = lista_msg
    for c in content:
        try:
            post(url, json={'username':'Mage', 'content':c})
            print(True)
        except Exception as e:
            print(str(e))
            print(False)
        sleep(1.26)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
