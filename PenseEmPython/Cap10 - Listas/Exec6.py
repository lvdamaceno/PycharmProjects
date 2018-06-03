word1 = 'banana'
word2 = 'ananab'


def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(is_anagram(word1, word2))