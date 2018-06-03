def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number
    """
    total = 0
    nova_lista = []
    for nested in t:
        print(nested)
        total += sum(nested)
        nova_lista.append(total)
        print(total)
    return nova_lista




t = [[1],[2],[3]]

print(nested_sum(t))