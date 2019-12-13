from ordering.get_card_order import get_card_order


def high_card(hand):

    cards = [card[0] for card in hand]

    ordered_cards = get_card_order()

    for ordered_card in reversed(ordered_cards):

        if ordered_card in cards:

            return ordered_card
