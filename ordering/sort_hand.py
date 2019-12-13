from ordering.get_card_order import get_card_order


def sort_hand(hand):

    sorted_hand = []

    card_order = get_card_order()

    for sort_count, sort_card in enumerate(card_order):

        for hand_count, hand_card in enumerate(hand):

            if sort_card == hand_card[0]:

                sorted_hand.append(hand_card)

    return sorted_hand
