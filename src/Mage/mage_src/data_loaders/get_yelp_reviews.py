from time import sleep
import pandas as pd
import requests

from mage_ai.data_preparation.shared.secrets import get_secret_value
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    """
    def get_yelp_reviews(business_id, API_KEY=get_secret_value('YELP_API_KEY')):
        """
        """
        url = f'https://api.yelp.com/v3/businesses/{business_id}/reviews?limit=50&sort_by=yelp_sort'
        headers = {'Authorization': f'Bearer {API_KEY}'}

        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            # Leer archivo de respuesta JSON 
            reviews_data = respuesta.json()
            # Extraer `reviews`
            reviews = reviews_data.get('reviews')
            return reviews
        else:
            return None

    
    df_darden_y_comp = pd.read_pickle('/home/data/df_darden_y_comp.pickle')
    df_api_reviews = pd.DataFrame()

    for b_id in df_darden_y_comp['business_id'].tolist():
        reviews = get_yelp_reviews(b_id)
        sleep(0.55)  # rate-limit, para evitar bloqueo de acceso API
        
        if not reviews:
            continue

        for i, r in enumerate(reviews):
            # Parse dia de la semana
            day = pd.to_datetime(r['time_created'])
            day_nombres = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            review = {
            'business_id': b_id,
            'review_id': r['id'],
            'user_id': r['user']['id'],
            'stars': float(r['rating']),
            'text': r['text'],
            'date': r['time_created'],
            'day': day_nombres[day.dayofweek]
            }

            df_api_reviews = pd.concat([df_api_reviews, pd.DataFrame(review, index=[i])])

    df = df_api_reviews.merge(df_darden_y_comp, on='business_id')
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
