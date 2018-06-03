fin = open("words.txt")

d = dict()

print(d)

d['a'] = '1'
d['b'] = '2'

print(d)

i = 1
for line in fin:
    word = line.strip()
    d[word] = i
    i += 1


print(d['ball'])