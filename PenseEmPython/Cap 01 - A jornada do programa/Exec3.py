"""
if you run 10 Km in 42 minutes and 42 seconds, what is your average step. in seconds, minutes and hour per miles?
"""


def mile(k):
    return k * 0.62


def seconds(m, s):
    return (m * 60) + s


print(mile(10))
print(seconds(42, 42))

print("Miles per minutes: " + str(mile(10) / 42))
print('Miles per second: ' + str(mile(10) / seconds(42, 42)))
