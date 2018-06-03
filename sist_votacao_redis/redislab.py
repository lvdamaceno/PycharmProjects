import redis
import random

r = redis.StrictRedis(host='localhost', port=6379,
                      charset="utf-8", decode_responses=True, db=0)
r.flushall()

# votacao = int(input('Quantas pessoas irão votar?'))
votacao = int(random.randint(1, 5000))

"""
votos = dict()
for i in range(votacao):
    voto = int(input(str(i+1) + ' Qual seu voto? 
    \n(1 - Candidato1 / 2 - Candidato2):' + '\n'))
    if voto not in votos:
        votos[voto] = 1
    else:
        votos[voto] += 1

print(votos)
"""

for i in range(votacao):
    user = str(random.randint(100000, 999999))
    """
    voto = int(input(user + ' Qual seu voto? '
                            '\n(1 - Candidato1 / 2 - Candidato2):' + '\n'))
    """
    voto = int(int(random.randint(1, 2)))
    r.set(user, voto)

allkeys = r.keys('*')
count = int(r.dbsize())

# print(allkeys)
# print(r.get(allkeys[0]))

c1 = 0
c2 = 0
for i in range(count):
    #print(str(allkeys[i]) + " - " + str(r.get(allkeys[i])))
    voto = int(r.get(allkeys[i]))
    if voto == 1:
        c1 += 1
    else:
        c2 += 1

print('Qtd de votos: ' + str(votacao))

if c1 == c2:
    print('Empatou')
elif c1 > c2:
    print('Candidato 1 foi campeão com ' + str(c1) + ' votos contra ' + str(c2))
else:
    print('Candidato 2 foi campeão com ' + str(c2) + ' votos contra ' + str(c1))
