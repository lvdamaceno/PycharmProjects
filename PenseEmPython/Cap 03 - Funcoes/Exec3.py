def header(qtd):
    if qtd == 1:
        print("+" + "-" * 4 + "+")
    else:
        print("+", end="")
        for qtd in range(qtd):
            print("-" * 4 + "+", end="")


def middle(qtd):
    if qtd == 1:
        print("|" + " " * 4 + "|")
    else:
        print("|", end="")
        for qtd in range(qtd):
            print(" " * 4 + "|", end="")


col = 2
lin = 2

for lin in range(lin):
    header(col)
    print("")
    for r in range(4):
        middle(col)
        print("")
header(col)
