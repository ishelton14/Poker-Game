from evaluate_hand import evaluate_hand
from ordering.get_card_order import get_card_order
from validators.highest_card import highest_card
from validators.get_tie_breaker import get_tie_breaker

with open('poker.txt', 'r') as fh:
    results = fh.read()

rows = results.splitlines()

card_order = get_card_order()

winners = []

for row in rows:

    hand = row.split(' ')

    player_a_hand = hand[0:5]
    player_b_hand = hand[5:10]

    player_a_score = evaluate_hand(player_a_hand)
    player_b_score = evaluate_hand(player_b_hand)

    # If neither player gets at least one pair, get highest card
    if player_a_score is None and player_b_score is None:
        winner = highest_card(player_a_hand, player_b_hand)

    # If player a or player b gets at least one pair, but the other player does not,
    # the player with at least one pair wins
    elif player_a_score is None and player_b_score is not None:
        winner = 1
    elif player_a_score is not None and player_b_score is None:
        winner = 0

    # If both players get at least one pair, check scores
    else:

        # Separate tie breaker and score value
        player_a_tie_breaker, player_a_score = get_tie_breaker(card_order, player_a_score)
        player_b_tie_breaker, player_b_score = get_tie_breaker(card_order, player_b_score)

        if player_a_score < player_b_score:
            winner = 0

        elif player_b_score < player_a_score:
            winner = 1

        else:

            # If both players have same the score and both have tie breaker values, then check tie breaker values
            if player_a_tie_breaker is not None and player_b_tie_breaker is not None:

                if player_a_tie_breaker > player_b_tie_breaker:
                    winner = 0
                elif player_b_tie_breaker > player_a_tie_breaker:
                    winner = 1
                else:
                    winner = highest_card(player_a_hand, player_b_hand)

            else:
                winner = highest_card(player_a_hand, player_b_hand)

    winners.append(winner)

answer = len([winner for winner in winners if winner == 0])

print('Player 1 won {} games.'.format(answer))
