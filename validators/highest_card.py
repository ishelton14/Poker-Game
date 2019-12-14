from validators.high_card import high_card
from ordering.get_card_order import get_card_order


def get_score(card_order, high):

    score = [count for count, card in enumerate(card_order)
             if card == high][0]

    return score


def highest_card(hand_a, hand_b):

    player_a_high = high_card(hand_a)
    player_b_high = high_card(hand_b)

    card_order = get_card_order()

    player_a_score = get_score(card_order, player_a_high)
    player_b_score = get_score(card_order, player_b_high)

    if player_a_score > player_b_score:
        winner = 0
    elif player_b_score > player_a_score:
        winner = 1
    # For a tie, return None
    else:
        winner = None

    return winner
