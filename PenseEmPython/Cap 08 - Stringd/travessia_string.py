fruit = "banana"

print(len(fruit))

print("")


index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print("")

fruit = "maracuja"
for letter in fruit:
    print(letter)


prefixes = "JKLMNOPQ"
suffix = "ack"
suffix2 = "uack"

print(" ")


for letter in prefixes:
    if letter != "O" and letter != "Q":
        print(letter + suffix)
    else:
        print(letter + suffix2)