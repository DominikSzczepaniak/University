from collections import deque 
slowa_lista_cala = set()
for line in open("slowa.txt"):
    slowa_lista_cala.add(line.rsplit()[0])

def shortest_path(start, end, words_list):
    # Sprawdzenie czy oba słowa są równej długości
    if len(start) != len(end):
        return []
    # Utworzenie kolejki 
    queue = deque([(start, [start])])
    # Utworzenie setu ze słowami, aby sprawdzanie było szybsze
    words = set(words_list)
    # Pętla szukająca
    while queue:
        word, path = queue.popleft()
        # Dla każdej pozycji w słowie
        for i in range(len(word)):
            # Dla każdej litery alfabetu
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                # jeśli nowe słowo jest w liście i nie jest już na liście
                if new_word in words and new_word not in path:
                    if new_word == end:
                        return path + [new_word]
                    queue.append((new_word, path + [new_word]))
    return []
print(shortest_path("mąka", "keks", slowa_lista_cala))
print(shortest_path("woda", "wino", slowa_lista_cala))
