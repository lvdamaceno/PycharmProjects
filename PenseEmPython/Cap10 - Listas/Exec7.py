def has_duplicates(t):
    t2 = sorted(t)
    for i in range(len(t2)-1):
        if t2[i] == t2[i+1]:
            return print("repetido")
    return print("ñ repetido")


t = [1, 60, 2, 4, 5, 3]
has_duplicates(t)

def has_duplicates2(s):

    t = list(s)
    t.sort()

    # check for adjacent elements that are equal
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

print(has_duplicates2(t))
