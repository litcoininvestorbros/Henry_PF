import pickle


def crear_brands_pickle() -> None:
    """Crea dos archivos pickle, 1) un dict de marcas correspondientes
    a Darden y sus competidores, 2)
    """
    # Diccionario de marcas de Darden y competidores
    dict_brands = {
        # Darden brands
        'darden': [
            "Olive Garden Italian Restaurant",
            "Olive Garden",
            "LongHorn Steakhouse",
            "Cheddar's Scratch Kitchen",
            "Yard House",
            "The Capital Grille",  # no esta en el dataset
            "Seasons 52",
            "Bahama Breeze",
            "Eddie V's",  # no esta en el dataset
            "Ruth's Chris Steak House"
        ],
        # Bloomin brands
        'bloomin': [
            "Outback Steakhouse",
            "Carrabba's Italian Grill",
            "Bonefish Grill",
            "Fleming's Prime Steakhouse & Wine Bar",
            "Aussie Grill",
            "Aussie Grill - Brandon"
        ],
        # Brinker brands
        'brinker': [
            "Chili's",  # aparece con 2 nombres distintos
            "Chili's Grill & Bar",  # aparece con 2 nombres distintos
            "Maggiano's Little Italy",
            "It's Just Wings"
        ],
        # Texas Roadhouse brands
        'texasroadhouse': [
            "Texas Roadhouse",
            "Bubba's 33",
            #"Jaggers"  # Fast food, excluir?   ####
        ]
    }

    lista_brands = [brand for lista in dict_brands.values() for brand in lista]

    with open('./assets/brands_dict.pickle', 'wb') as f:
        pickle.dump(dict_brands, f, protocol=pickle.HIGHEST_PROTOCOL)

    with open('./assets/brands_list.pickle', 'wb') as f:
        pickle.dump(lista_brands, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    crear_brands_pickle()