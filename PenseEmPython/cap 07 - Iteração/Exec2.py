import math

print(eval("1 + 2 * 3"))

print(eval("math.sqrt(5)"))

print(eval("type(math.pi)"))

def eval_loop():
    while True:
        line = input("> ")
        if line == "done":
            break
        print(eval(line))
    print("Done!")

eval_loop()