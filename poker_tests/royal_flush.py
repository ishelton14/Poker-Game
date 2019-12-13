from validators.same_suit import same_suit


def royal_flush(hand):

    royal_flush_sequence = ('T', 'J', 'Q', 'K', 'A')

    # If any card is not a Ten, Jack, Queen, King, or Ace then return False
    for card in hand:

        if card[0] not in royal_flush_sequence:

            return False

    if not same_suit(hand):

        return False

    return True
