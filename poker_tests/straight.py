from ordering.sort_hand import sort_hand
from ordering.get_card_order import get_card_order


def straight(hand):

    hand = sort_hand(hand)
    hand = ''.join([str(card[0]) for card in hand])

    card_order = get_card_order()
    card_order = ''.join([str(card) for card in card_order])

    if hand in card_order:

        return True

    return False
