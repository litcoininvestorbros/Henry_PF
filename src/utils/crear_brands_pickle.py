import pickle


def main() -> None:
    """Crea un archivo pickle de un dict de marcas correspondientes
    a Darden y sus competidores.
    """
    # Diccionario de marcas de Darden y competidores
    brands = {
        # Darden brands
        'darden': [
            "Olive Garden Italian Restaurant",
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

    with open('brands.pickle', 'wb') as handle:
        pickle.dump(brands, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()