from validators.same_suit import same_suit


def is_royal_flush(hand):

    royal_flush = ('T', 'J', 'Q', 'K', 'A')

    # If any card is not a Ten, Jack, Queen, King, or Ace then return False
    for card in hand:

        if card[0] not in royal_flush:

            return False

    if not same_suit(hand):

        return False

    return True
