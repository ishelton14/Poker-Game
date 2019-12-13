from poker_tests.is_straight import is_straight
from validators.same_suit import same_suit


def is_straight_flush(hand):

    return is_straight(hand) and same_suit(hand)
