def difference(original_sequence, expected_sequence):
    suma = 0
    for i in range(len(expected_sequence)):
        if original_sequence[i] != expected_sequence[i]:
            suma += 1
    return suma


def opt_dist(list, m):
    # dostajemy ciag 0 i 1 oraz liczbe m
    # chcemy poznac najmniejsza liczbe operacji aby miec po kolei m 1
    # czyli np dla 0001001 m = 4 mamy 2 operacje - zmiana 5 i 6 elementu z 0 na 1.

    # pomysl1: stworz wszystkie ciagi 0 i 1 ktore maja m jedynek po sobie, czyli np dla m=6 i dlugosci = 8:
    # 11111100, 01111110, 00111111
    # pozniej na podstawie tego mozemy napisac funkcje ktora sprawdza w ilu miejscach sie roznia
    # od siebie dwa ciagi i na podstawie tego znalezc minimalna odpowiedz
    n = len(list)
    if type(list) is not str:
        list = "".join(map(str, list))
    sequences = []
    for i in range(0, n - m + 1):
        left = i
        right = n - i - m
        ans = left * "0" + m * "1" + right * "0"
        sequences.append(ans)
    answer = n
    for i in sequences:
        answer = min(difference(list, i), answer)
    return answer


file = open("zad4_input.txt", "r")
answers = ""
for line in file:
    list, m = line.split()
    score = opt_dist(list, int(m))
    answers += (str(score) + "\n")
file = open("zad4_output.txt", "w")
file.write(answers)
