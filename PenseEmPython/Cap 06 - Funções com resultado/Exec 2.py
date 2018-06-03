"""
Função de Ackermann

A(m,n) =

    n + 1                   se m = 0
    A(m - 1,1)              se m > 0 e n = 0
    A(m - 1, A(m, n - 1))   se m > 0 e n > 0
"""


def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


print(ack(1, 1))
