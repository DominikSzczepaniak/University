words_set = set()
for line in open("words_for_ai1.txt", "r"):
    words_set.add(line.strip())
longest_word_length = max(words_set, key=len)
longest_word_length = len(longest_word_length)

def calculate_dp(wyraz):
    dp = [[] for i in range(len(wyraz))]
    for i in range(len(wyraz)):
        for j in range(min(longest_word_length, len(wyraz) - i), 0, -1):
            if wyraz[i:i + j] in words_set:
                dp[i].append(j)
        dp[i].sort(reverse=True)
    return dp

def correct_answer(word, choosen_words):
    Sum = 0
    for i in choosen_words:
        Sum += len(i)
    if Sum == len(word):
        return True
    return False

def backtrack(position, word, dp, choosen_words, current_answer, answers):
    if position in answers:
        if current_answer < answers[position]:
            return []
        else:
            answers[position] = current_answer
    else:
        answers[position] = current_answer
    results = []
    if position >= len(word):
        if correct_answer(word, choosen_words):
            results.append((choosen_words, current_answer))
    else:
        for i in dp[position]:
            score = backtrack(position + i, word, dp, choosen_words + [word[position:position + i]],
                                current_answer + i * i, answers)
            if score is not None:
                results.extend(score)
    return results

def solve(word):
    dp = calculate_dp(word)
    a = backtrack(0, word, dp, [], 0, {})
    a.sort(key=lambda x: x[1], reverse=True)
    score = a[0][0]
    answer = " ".join(score)
    return answer


def data_input():
    answers = []
    words = []
    for line in open("zad2_input.txt", "r"):
        word = line.strip()
        words.append(word)
    for word in words:
        answer = solve(word)
        answers.append(answer)
    f = open("zad2_output.txt", "w")
    for answer in answers:
        f.write(answer + " \n")


data_input()
