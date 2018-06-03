import math
import random


def mysqrt(a):
    x = random.randint(1, 100)
    while True:
        y = (x + a / x) / 2
        if y == x:
            return x
        x = y


x = 9

for a in range(x):
    a = a+1
    print(a, end=" | ")
    print(mysqrt(a), end=" | ")
    print(math.sqrt(a), end=" | ")
    print(abs(mysqrt(a) - math.sqrt(a)))


