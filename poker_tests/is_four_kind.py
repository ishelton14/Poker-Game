from validators.multiples import multiples


def is_four_kind(hand):

    similarities = multiples(hand)

    for similarity in similarities:

        if similarity.get('similarities') == 4:

            return True

    return False
