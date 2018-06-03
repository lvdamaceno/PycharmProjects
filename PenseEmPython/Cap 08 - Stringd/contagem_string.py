def count(word, letter, indice):
    word = word[indice:]
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)


word = "antonela"
count(word, "v", 0)
