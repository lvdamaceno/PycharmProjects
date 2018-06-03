def rotate_word(word, steps):
    for letter in word:
        print(chr(ord(letter) + steps), end="")


rotate_word("Vinicius", 2)