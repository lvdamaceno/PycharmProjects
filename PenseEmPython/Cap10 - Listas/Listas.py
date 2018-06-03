number_list = [10, 20, 30, 40]

print(number_list)
print(number_list[0])


words_list = ["nique", "pencil", "sound"]

print(words_list)
print(words_list[0])

variable_list = ['spam', 10, [2.0, 5]]

print(variable_list)
print(variable_list[-1])

empty = []

print(number_list, words_list, variable_list, empty)

words_list[1] = "eraser"
print(words_list)

cheeses = ['Cheddar', 'Edam', 'Gouda']
if 'Edam' in cheeses:
    print(True)
else:
    print(False)


for cheese in cheeses:
    print(cheese, end=" ")


print("")


