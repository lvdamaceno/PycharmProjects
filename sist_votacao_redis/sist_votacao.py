import redis
import random

r = redis.StrictRedis(host='localhost', port=6379,
                      charset="utf-8", decode_responses=True, db=0)
r.flushall()


def qtd_votos(limite):
    qtd = int(random.randint(1, limite))
    return qtd


def votacao(qtd):
    for i in range(qtd):
        user = str(random.randint(100000, 999999))
        voto = int(int(random.randint(1, 2)))
        r.set(user, voto)
    print('Qtd de votos: ' + str(qtd))


def apuracao():
    c1 = 0
    c2 = 0
    for i in range(count):
        # recebe o valor da chave na posição i
        voto = int(r.get(allkeys[i]))
        # se o valor do voto for igual à 1 itera na C1 se não na C2
        if voto == 1:
            c1 += 1
        else:
            c2 += 1
    return [c1, c2]


def resultado(c1, c2):
    # faz a comparação entre os votos e diz quem foi o vencedor.
    if c1 == c2:
        print('Empatou')
    elif c1 > c2:
        print('Candidato 1 foi campeão com ' + str(c1) + ' votos contra ' + str(c2))
    else:
        print('Candidato 2 foi campeão com ' + str(c2) + ' votos contra ' + str(c1))


qtd_votos = qtd_votos(100)

votacao(qtd_votos)

# cria um lista com as chaves
allkeys = r.keys('*')

# recebe o tamanho do banco
count = int(r.dbsize())

t = apuracao()

c1 = t[0]
c2 = t[1]

resultado(c1, c2)