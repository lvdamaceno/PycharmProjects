eng2sp = dict()

eng2sp['one'] = 'uno'

print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

print(eng2sp)

print(eng2sp['two'])

print(len(eng2sp))

print('one' in eng2sp)
print('uno' in eng2sp)

vals = eng2sp.values()
print('uno' in vals)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


print(histogram('banana'))

h = histogram('banana')
print(h)
print(h.get('a', 0))
print(h.get('b', 0))


def print_hist(h):
    for c in h:
        print(c, h[c])


print('')
h = histogram('parrot')
print(h)
print_hist(h)
print('')


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

k = reverse_lookup(h, 2)
print(k)
