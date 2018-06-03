def do_twice(f, q):
    f()
    f()


def print_spam():
    print("spam*")


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice(print_spam, 4)

print_twice("spam+")

do_twice(print_twice("spam/"), 2)
