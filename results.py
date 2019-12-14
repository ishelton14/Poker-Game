from evaluate_hand import evaluate_hand


with open('poker.txt', 'r') as fh:
    results = fh.read()

rows = results.splitlines()

for row in rows:

    hand = row.split(' ')

    evaluate_hand(hand[0:5])
    evaluate_hand(hand[5:10])

    break

