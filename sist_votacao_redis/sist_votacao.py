import redis
import random

# conexão ao banco redis (Java sucks)
r = redis.StrictRedis(host='localhost', port=6379,
                      charset="utf-8", decode_responses=True, db=0)
# limpa o banco
r.flushall()


def votacao(limite, id_inicio, id_final):
    """
    Povoa o banco com valores de votação randomicos, cria os valores
    id de usuarios ficticios, visto um range passado e seta no banco ao final
    :param limite: int de limite de votações
    :param id_inicio: int com um valor inicial qualquer
    :param id_final: int com um valor final qualquer
    :return: none
    """
    qtd = int(random.randint(1, limite))
    for i in range(qtd):
        user = str(random.randint(id_inicio, id_final))
        voto = int(int(random.randint(1, 2)))
        r.set(user, voto)
    print('Qtd de votos: ' + str(qtd))


def resultado():
    """
    inicializa duas variaveis para receber a contagem de votos para
    c1 e c2, count recebe o tamanho do banco e allkeys os valores das
    chaves em um lista. o laço for percorre allkeys e guarda o valor na
    variavel voto e entra no laço if, se voto for um itera em c1,
    do contrario itera em c2.
    :return: um list contendo a qtd de votos para c1 e c2
    """
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
    return decisao(c1, c2)


def decisao(c1, c2):
    """
    Faz a comparação entre os votos e diz quem foi o vencedor.
    :param c1: int, qtd de votos para c1
    :param c2: int, qtd de votos para c2
    :return: none
    """
    if c1 == c2:
        print('Empatou, ' + str(c1) + ' = ' + str(c2))
    elif c1 > c2:
        print('Candidato 1 foi campeão com ' + str(c1) + ' votos contra ' + str(c2))
    else:
        print('Candidato 2 foi campeão com ' + str(c2) + ' votos contra ' + str(c1))


# calcula o range de votação, informa na função para rodar as votações
votacao(1000, 100000, 999999)

# Efetua a apuração dos votos e retorna o vencedor
resultado()
