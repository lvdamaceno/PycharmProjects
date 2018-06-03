def nested_sum(list):
    """return sum(list)"""
    for i in list:
        print(i)


t = [[1, 2], [3], [4, 5, 6]]

a = [[1], [2], [3, 4]]


def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number
    """
    total = 0
    for nested in t:
        print(nested)
        total += sum(nested)
        print(total)
    return total

print(nested_sum(a))