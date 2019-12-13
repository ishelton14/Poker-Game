from poker_tests.straight import straight
from validators.same_suit import same_suit


def straight_flush(hand):

    return straight(hand) and same_suit(hand)
