fin = open("words.txt")


def biggerthen(size):
    for line in fin:
        word = line.strip()
        if len(word) >= size:
            print(word)


def count_lines():
    count = 0
    for line in fin:
        count = count + 1
    print(count)


def has_no_letter(letter):
    count = 0
    for line in fin:
        word = line.strip()
        if letter not in word:
            print(word)
            count = count + 1
    percent = (count * 100) / 113809
    print("There is only " + str(percent) + "% words with no " + letter)


def avoids0(word, letters):
    for letter in letters:
        if letter not in word:
            print("não tem", end=" ")
            print(letter)
        else:
            print("tem", end=" ")
            print(letter)


def avoids(letters):
    for line in fin:
        word = line.strip()
        for letter in letters:
            if letter not in word:
                print(word, end=" ")
                print("não tem", end=" ")
                print(letter)
            else:
                print(word, end=" ")
                print("tem", end=" ")
                print(letter)


avoids("ab")
