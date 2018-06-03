def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True


def avoids(word, forbiden):
    for letter in word:
        if letter in forbiden:
            return False
    return True


def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True


def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


def uses_all_0(word, required):
    return uses_only(required, word)


def is_abcdarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


def is_abcdarian_0(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abcdarian_0(word[1:])


def is_abcdarian_1(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i + 1
    return True



print(is_abcdarian("abcda"))