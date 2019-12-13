from poker_tests.is_straight import is_straight
from poker_tests.is_royal_flush import is_royal_flush


def compare_hands(hand_a, hand_b):

    # Check royal flush
    is_royal_flush(hand_a)

    # Check straight
    is_straight(hand_a)


# a = ['9S', 'JS', 'QS', 'KS', 'AS']
# a = ['JS', 'QS', 'KS', 'AS', 'TS']
a = ['2S', '4S', '3S', '5S', '6S']

print(is_straight(a))


