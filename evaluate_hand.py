from poker_tests.royal_flush import royal_flush
from poker_tests.straight_flush import straight_flush
from poker_tests.four_kind import four_kind
from poker_tests.full_house import full_house
from validators.same_suit import same_suit
from poker_tests.straight import straight
from poker_tests.three_kind import three_kind
from poker_tests.two_pair import two_pair
from poker_tests.one_pair import one_pair


def evaluate_hand(hand):

    evaluate_functions = [royal_flush, straight_flush, four_kind, full_house,
                          same_suit, straight, three_kind, two_pair, one_pair]

    for count, func in enumerate(evaluate_functions):

        if func(hand) is True:

            return count

        # If hand requires a tie breaker, return both count and tie breaker value
        elif type(func(hand)) is tuple:

            return count, func(hand)[1]
