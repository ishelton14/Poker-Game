from validators.highest_card import get_score


def get_tie_breaker(card_order, score):

    if type(score) is tuple:
        tie_breaker = score[1]
        tie_breaker = get_score(card_order, tie_breaker)
        score = score[0]

        return tie_breaker, score

    return None, score
