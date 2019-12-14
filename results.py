from evaluate_hand import evaluate_hand
from validators.highest_card import highest_card


with open('poker.txt', 'r') as fh:
    results = fh.read()

rows = results.splitlines()

winners = []

for row in rows:

    hand = row.split(' ')

    player_a_hand = hand[0:5]
    player_b_hand = hand[5:10]

    player_a_score = evaluate_hand(player_a_hand)
    player_b_score = evaluate_hand(player_b_hand)

    if player_a_score is None and player_b_score is None:
        winner = highest_card(player_a_hand, player_b_hand)

    elif player_a_score is None and player_b_score is not None:
        winner = 1

    elif player_a_score is not None and player_b_score is None:
        winner = 0

    else:

        # If both players have at least a pair, return the lowest number
        if player_a_score < player_b_score:
            winner = 0

        elif player_b_score < player_a_score:
            winner = 1

        else:
            winner = highest_card(player_a_hand, player_b_hand)

    winners.append(winner)

    break

answer = len([winner for winner in winners if winner == 0])

print(answer)

