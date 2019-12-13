def multiples(hand):

    cards = [card[0] for card in hand]

    unique_cards = list(set(cards))

    multiple_cards = []

    for unique_card in unique_cards:

        similarities = len([card for card in cards if card == unique_card])

        multiple_cards.append(dict(card=unique_card, similarities=similarities))

    return multiple_cards
