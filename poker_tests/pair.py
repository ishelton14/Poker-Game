from validators.multiples import multiples
from ordering.get_card_order import get_card_order
from validators.highest_card import get_score


def pair(hand, pair_number):

    similarities = multiples(hand)

    if len([card.get('similarities') for card in similarities
            if card.get('similarities') == 2]) == pair_number:

        highest_rank = '2'
        card_order = get_card_order()

        # Get highest ranked pair
        for similarity in similarities:
            if similarity.get('similarities') == 2:
                if get_score(card_order, similarity.get('card')) > get_score(card_order, highest_rank):
                    highest_rank = similarity.get('card')

        return True, highest_rank

    return False
