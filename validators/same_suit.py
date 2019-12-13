def same_suit(hand):

    # Get just suits
    suits = [card[1] for card in hand]

    # If not all suits are the same then return False
    unique_suits = set(suits)

    if len(unique_suits) > 1:

        return False

    return True
