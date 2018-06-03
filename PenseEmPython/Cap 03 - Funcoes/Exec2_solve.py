def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func: object, arg: object) -> object:
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print_twice, "spam*")
print("")

do_four(print_twice, "spam")
