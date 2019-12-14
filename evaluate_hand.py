from poker_tests.royal_flush import royal_flush
from poker_tests.straight_flush import straight_flush
from poker_tests.straight import straight
from poker_tests.four_kind import four_kind
from poker_tests.full_house import full_house
from validators.same_suit import same_suit
from poker_tests.three_kind import three_kind
from poker_tests.two_pair import two_pair
from poker_tests.one_pair import one_pair


def evaluate_hand(hand):

    evaluate_functions = [royal_flush, straight_flush, straight, four_kind, full_house,
                          same_suit, three_kind, two_pair, one_pair]

    for count, func in enumerate(evaluate_functions):

        if func(hand) is True:

            return count

    # royal_flush(hand)
    #
    # straight_flush(hand)
    #
    # four_kind(hand)
    #
    # full_house(hand)
    #
    # # Flush
    # same_suit(hand)
    #
    # straight(hand)
    #
    # three_kind(hand)
    #
    # # Two pair
    # pair(hand, pair_number=2)
    #
    # # One pair
    # pair(hand, pair_number=1)
    #
    # high_card(hand)


# Royal Flush
# a = ['TS', 'JS', 'QS', 'KS', 'AS']

# Straight Flush
# a = ['9S', 'TS', 'JS', 'QS', 'KS']

# a = ['2S', '4S', '3S', '5S', '6S']

# Four of a kind
# a = ['2S', '2C', '2D', '5S', '2H']

# Full house
# a = ['2S', '2C', '2D', '5S', '5H']

# Flush
# a = ['1C', '3C', '5C', '6C', '9C']

# Three of a kind
# a = ['2S', '2C', '4D', '5S', '2H']

# Two pair
# a = ['2S', '2C', '5D', '3S', '3H']

# One pair
# a = ['2S', '2C', '5D', '4S', '7H']

# High Card
# a = ['2S', '2C', '5D', '4S', 'KH']

# result = evaluate_hand(a)
#
# print(result)
