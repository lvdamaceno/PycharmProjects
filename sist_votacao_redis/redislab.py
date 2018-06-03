import redis
# importando o random para não ter que ficar digitando os usuários e votos
import random

# conexão com o banco (java sucks!)
r = redis.StrictRedis(host='localhost', port=6379,
                      charset="utf-8", decode_responses=True, db=0)
# zerando o banco antes da votação
r.flushall()

# comando anterior para perguntar quantas pessoas votariam
# votacao = int(input('Quantas pessoas irão votar?'))

# criando um range de votações
votacao = int(random.randint(1, 5000))

"""
# primeira tentativa usando dicionário
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

""" 
esse for recebe a quantidade de votações à serem feitas,
usa o range para criar umas id's fakes para usuários
e também para escolher os votos entre 1 e 2
ao final registra no banco o usuario e o voto escolhido.
"""
for i in range(votacao):
    user = str(random.randint(100000, 999999))
    voto = int(int(random.randint(1, 2)))
    r.set(user, voto)

# cria um lista com as chaves
allkeys = r.keys('*')

# recebe o tamanho do banco
count = int(r.dbsize())

# print(allkeys)
# print(r.get(allkeys[0]))

# inicializa os candidatos como 0 para receber os votos
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

print('Qtd de votos: ' + str(votacao))

# faz a comparação entre os votos e diz quem foi o vencedor.
if c1 == c2:
    print('Empatou')
elif c1 > c2:
    print('Candidato 1 foi campeão com ' + str(c1) + ' votos contra ' + str(c2))
else:
    print('Candidato 2 foi campeão com ' + str(c2) + ' votos contra ' + str(c1))
