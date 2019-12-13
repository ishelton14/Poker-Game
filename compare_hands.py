from poker_tests.is_royal_flush import is_royal_flush
from poker_tests.is_straight_flush import is_straight_flush
from poker_tests.is_straight import is_straight
from poker_tests.is_four_kind import is_four_kind
from poker_tests.is_full_house import is_full_house
from validators.same_suit import same_suit
from poker_tests.is_three_kind import is_three_kind
from poker_tests.is_pair import is_pair
from validators.high_card import high_card


def compare_hands(hand_a, hand_b=None):

    is_royal_flush(hand_a)

    is_straight_flush(hand_a)

    is_four_kind(hand_a)

    is_full_house(hand_a)

    # Flush
    same_suit(hand_a)

    is_straight(hand_a)

    is_three_kind(hand_a)

    # Two pair
    is_pair(hand_a, pair_number=2)

    # One pair
    is_pair(hand_a, pair_number=1)

    high_card(hand_a)


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
a = ['2S', '2C', '5D', '4S', 'KH']

print(compare_hands(a))
