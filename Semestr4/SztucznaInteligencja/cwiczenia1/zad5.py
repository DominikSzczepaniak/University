# blotkarz wygrywa tylko gdy:
# 1. ma 5 kart tego samego koloru z rzedu
# 2. 4 karty tego samego typu
# 3. ma full house
# 4. ma 5 kart tego samego koloru (nie z rzedu)
# 5. ma 5 kart z rzedu
# 6. trojka
# 7. dwie pary
# 8. para

# blotkarz wygrywa tylko gdy wartosc jego ukladu jest wyzej niz uklad figuranta w powyzszej liscie
import random
from itertools import permutations, product, combinations

blotkarz_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#blotkarz_cards = [8,9,10] #wygrywa statystycznie
figurant_cards = [11, 12, 13, 14]
colors1 = ["c", "d", "h", "s"]
colors2 = ["c", "d", "h", "s"]


def first_case(cards):
    if (fourth_case(cards) and fifth_case(cards)):
        return True
    return False


def second_case(cards):
    cards = [int(x[0]) for x in cards]
    for i in range(2):
        if cards.count(cards[i]) == 4:
            return True
    return False


def third_case(cards):
    if (sixth_case(cards) and eighth_case(cards)):
        return True
    return False


def fourth_case(cards):
    cols = [x[1] for x in cards]
    if (cols.count(cols[0]) == 5):
        return True
    return False


def fifth_case(cards):
    cards = sorted(cards, key=lambda x: int(x[0]))
    for i in range(1, len(cards)):
        if int(cards[i][0]) - int(cards[i - 1][0]) != 1:
            return False
    return True


def sixth_case(cards):
    cards = [int(x[0]) for x in cards]
    for i in range(3):
        if cards.count(cards[i]) == 3:
            return True
    return False


def seventh_case(cards):
    cards = [int(x[0]) for x in cards]
    cards.sort()
    pairs = 0
    for i in range(1, len(cards)):
        if cards[i] == cards[i - 1]:
            pairs += 1
    if pairs == 2:
        return True
    return False


def eighth_case(cards):
    cards = [int(x[0]) for x in cards]
    for i in range(4):
        if cards.count(cards[i]) == 2:
            return True
    return False


def check_point(cards):
    if (first_case(cards)):
        return 9
    if (second_case(cards)):
        return 8
    if (third_case(cards)):
        return 7
    if (fourth_case(cards)):
        return 6
    if (fifth_case(cards)):
        return 5
    if (sixth_case(cards)):
        return 4
    if (seventh_case(cards)):
        return 3
    if (eighth_case(cards)):
        return 2
    return 1


def rozwaz_wszystkie_mozliwosci():
    #sprawdz wszystkie mozliwosci dla blotkarza i figuranta i sprawdz jak czesto wygrywa jeden a jak czesto wygrywa drugi
    #dla kazdej mozliwosci
    blotkarz_wins = 0
    figurant_wins = 0
    figurant_perms = list(combinations(product(figurant_cards, colors1), 5))
    blotkarz_perms = list(combinations(product(blotkarz_cards, colors2), 5))
    #zapiszmy to jako sily talii (checkpoints)
    blotkarz_perms_points = [check_point(x) for x in blotkarz_perms]
    figurant_perms_points = [check_point(x) for x in figurant_perms]
    blotkarz_ile = [blotkarz_perms_points.count(i) for i in range(1, 10)]
    figurant_ile = [figurant_perms_points.count(i) for i in range(1, 10)]
    for i in range(1, 10):
        #jak blotkarz ma 1 to znaczy ze nie wygral ani razu z tym ukladem
        if(i == 1):
            figurant_wins += figurant_ile[i - 1]
            continue
        #blotkarz wygrywa z figurantem dla kazdego ukladu > od figuranta
        #figurant wygrywa dla kazdego ukladu >= od blotkarza
        for j in range(1, i):
            blotkarz_wins += blotkarz_ile[i - 1] * figurant_ile[j - 1]
        for j in range(1, i+1):
            figurant_wins += figurant_ile[i - 1] * blotkarz_ile[j - 1]
    print("Blotkarz wins: ", blotkarz_wins)
    print("Figurant wins: ", figurant_wins)
    print("Games: ", blotkarz_wins+figurant_wins)
    print("prawdopodobienstwo blotkarza: ", blotkarz_wins/(blotkarz_wins+figurant_wins))





rozwaz_wszystkie_mozliwosci()
