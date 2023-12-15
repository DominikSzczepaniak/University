def is_palindrom(text):
    word = text.lower()
    zamiana = [" ", ",", ".", "!", "?", ":"]
    for i in zamiana:
        word = word.replace(i, "")
    word = word.split()
    for i in word:
        if i != i[::-1]:
            return False
    return True

print(is_palindrom("Kobyła ma mały bok"))
print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))