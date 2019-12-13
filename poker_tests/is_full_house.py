from validators.multiples import multiples


def is_full_house(hand):

    similarities = multiples(hand)

    three_kind = False
    two_kind = False

    for similarity in similarities:

        if similarity.get('similarities') == 3:

            three_kind = True

        elif similarity.get('similarities') == 2:

            two_kind = True

    return three_kind and two_kind
