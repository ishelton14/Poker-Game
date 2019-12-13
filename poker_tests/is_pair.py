from validators.multiples import multiples


def is_pair(hand, pair_number):

    similarities = multiples(hand)

    if len([card.get('similarities') for card in similarities
            if card.get('similarities') == 2]) == pair_number:

        return True

    return False
