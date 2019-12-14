from validators.multiples import multiples


def four_kind(hand):

    similarities = multiples(hand)

    for similarity in similarities:

        if similarity.get('similarities') == 4:

            # Return value of rank in addition to boolean value
            return True, similarity.get('card')

    return False
