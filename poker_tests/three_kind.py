from validators.multiples import multiples


def three_kind(hand):

    similarities = multiples(hand)

    # Ensure there are not multiple pairs
    if len([card.get('similarities') for card in similarities
            if card.get('similarities') > 1]) > 1:

        return False

    for similarity in similarities:

        if similarity.get('similarities') == 3:

            return True

    return False
