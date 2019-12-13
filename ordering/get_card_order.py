def get_card_order():

    number_cards = list(range(2, 10))
    number_cards = [str(card) for card in number_cards]
    face_cards = ['T', 'J', 'Q', 'K', 'A']

    card_order = number_cards + face_cards

    return card_order
