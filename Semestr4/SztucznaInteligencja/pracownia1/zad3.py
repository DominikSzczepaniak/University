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


def szanse_normalne(n):
    ilosc_losowan = n
    ilosc_wygranych = 0
    for i in range(ilosc_losowan):
        cards1 = []
        cards2 = []
        uzyte1 = set()
        uzyte2 = set()
        for j in range(5):
            wartosc1 = 0
            kolor1 = 0
            wartosc2 = 0
            kolor2 = 0
            while True:
                wartosc1 = random.choice(blotkarz_cards)
                kolor1 = random.choice(colors1)
                if (wartosc1, kolor1) not in uzyte1:
                    uzyte1.add((wartosc1, kolor1))
                    break
            while True:
                wartosc2 = random.choice(figurant_cards)
                kolor2 = random.choice(colors2)
                if (wartosc2, kolor2) not in uzyte2:
                    uzyte2.add((wartosc2, kolor2))
                    break
            cards1.append((wartosc1, kolor1))
            cards2.append((wartosc2, kolor2))
        # print(cards1, cards2)
        if check_point(cards1) > check_point(cards2):
            ilosc_wygranych += 1
    return ilosc_wygranych / ilosc_losowan


print(szanse_normalne(50000))
