from compare_hands import compare_hands


with open('poker.txt', 'r') as fh:
    results = fh.read()

rows = results.splitlines()

for row in rows:

    hand = row.split(' ')

    compare_hands(hand[0:5], hand[5:10])

    break

