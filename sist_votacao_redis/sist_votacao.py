import redis
import random

r = redis.StrictRedis(host='localhost', port=6379,
                      charset="utf-8", decode_responses=True, db=0)
r.flushall()


def qtd_votos(limite):
    qtd = int(random.randint(1, limite))
    return qtd


def votacao(qtd, id_inicio, id_final):
    for i in range(qtd):
        user = str(random.randint(id_inicio, id_final))
        voto = int(int(random.randint(1, 2)))
        r.set(user, voto)
    print('Qtd de votos: ' + str(qtd))


def apuracao():
    c1 = 0
    c2 = 0
    count = int(r.dbsize())
    allkeys = r.keys('*')
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
        print('Empatou, ' + str(c1) + ' = ' + str(c2))
    elif c1 > c2:
        print('Candidato 1 foi campeão com ' + str(c1) + ' votos contra ' + str(c2))
    else:
        print('Candidato 2 foi campeão com ' + str(c2) + ' votos contra ' + str(c1))


qtd_votos = qtd_votos(100)

votacao(qtd_votos, 100000, 999999)

t = apuracao()

resultado(t[0], t[1])
