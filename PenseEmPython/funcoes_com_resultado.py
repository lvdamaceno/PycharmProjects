import math

"funções com valores de retorno"


def area(radius):
    a = math.pi * radius ** 2
    return a


def area1(radius):
    return math.pi * radius ** 2


print(area(15))
print(area1(15))


def absolute_value(x):
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x


print(absolute_value(-10))
print(absolute_value(10))
print(absolute_value(0))


def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


print(compare(5, 4))
print(compare(4, 4))
print(compare(4, 5))

"funções booleanas"


def is_divisible_old(x, y):
    if x % y == 0:
        return True
    else:
        return False


print(is_divisible_old(6, 4))
print(is_divisible_old(6, 3))


def is_divisible(x, y):
    return x % y == 0


print(is_divisible(6, 4))
print(is_divisible(6, 3))

"""
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False
"""


def is_between(x, y, z):
    return x <= y <= z


a = 1
b = 2
c = 3
print(str(a) + " < " + str(b) + " < " + str(c) + " is " + str(is_between(a, b, c)))
print(str(a) + " < " + str(b) + " < " + str(c) + " is " + str(is_between(b, c, a)))

