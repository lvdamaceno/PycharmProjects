# conexão com o banco
from cassandra.cluster import Cluster

cluster = Cluster()
# criar o banco antes
session = cluster.connect('aula')


# funções de auxílio


# limpa as tabela
def clean():
    session.execute("TRUNCATE playlist_atual;")
    session.execute("TRUNCATE playlist_versionada")


# printa o estado atual da tabela
def print_table():
    playlist = session.execute("select * from playlist_atual;")
    for musicas in playlist:
        print(musicas.id_playlist, musicas.posicao, musicas.album, musicas.artista, musicas.id_musica, musicas.nome)
    print(" ")


# insere mais rapidamente as musicas na tabela playlist_atual
def insere_todas():
    musicas = ['Help!', 'Blackbird', 'Something', 'Yesterday']
    for musica in musicas:
        adicionar(musica, 1)
    print_table()


# funções de verificação, inserção, remoção, troca e atualização de versão

# verifica a existencia de uma musica na tabela
def verifica(musica, id_playlist):
    playlist_atual = session.execute("select * from playlist_atual where nome = '{0}' "
                                     "and id_playlist={1} allow filtering;".format(musica, id_playlist))
    if not playlist_atual.current_rows:
        return False
    else:
        return True


# função para adicionar novas musicas à tabela
def adicionar(nova_musica, id_lista):
    musica = nova_musica
    # verifica se a musica já existe
    if verifica(musica, id_lista) is True:
        return print("Essa musica já existe")
    else:
        # verifica a ultima posicao na playlist, se for zero começa do 1
        # se for mair que 1 vai iterando
        # utlizando o codigo da id da playlist a função filtra antes de começar tudo para que numeração de posicao
        # seja diferente para cada playlist
        playlist_atual = session.execute(
            "select * from playlist_atual where id_playlist={0} allow filtering".format(id_lista))
        # se o retorno da linha abaixo for uma lista vazia ele considera que nao exitem
        # registro na tabela, entao saré o primeiro
        if not playlist_atual.current_rows:
            posicao_atual = 0
            # print(posicao_atual)
        else:
            for dados in playlist_atual:
                pos = session.execute(
                    "select max(posicao) from playlist_atual where id_playlist={0} allow filtering".format(id_lista))
                # precisa achar uma forma melhor de pegar esse valor
                posicao_atual = pos.current_rows[0][-1]
        # à partir daque que começa a inserção das musicas
        musicas = session.execute("select * from musicas where nome='{0}' allow filtering".format(musica))
        for musica in musicas:
            id_playlist = id_lista
            # if para verificar se a tabela é vazia ou não
            if posicao_atual == 0:
                posicao = 1
            else:
                posicao = posicao_atual + 1
            album = musica.album
            artista = musica.artista
            id_musica = musica.id
            nome_musica = musica.nome
            session.execute("insert into playlist_atual(id_playlist, posicao, album, artista, id_musica, nome)"
                            "values ({0}, {1}, '{2}', '{3}', {4}, '{5}')".format
                            (id_playlist, posicao, album, artista, id_musica, nome_musica))
            atualiza_versao(id_lista, 'ADI({0})'.format(nome_musica))


# atualiza a tabela de versionamento da playlist
def atualiza_versao(id_playlist, modificacao):
    versao = session.execute(
        "select * from playlist_versionada where id_playlist={0} allow filtering".format(id_playlist))
    # print(versao.current_rows)
    if not versao.current_rows:
        session.execute("insert into playlist_versionada (id_playlist, versao, modificacao)"
                        "values({0}, {1}, '{2}')".format(id_playlist, 1, modificacao))
    else:
        versao = session.execute(
            "select max(versao) from playlist_versionada where id_playlist={0} allow filtering".format(id_playlist))
        session.execute("insert into playlist_versionada (id_playlist, versao, modificacao)"
                        "values({0}, {1}, '{2}')".format(id_playlist, versao.current_rows[0][-1] + 1, modificacao))
        # print(versao.current_rows[0][-1])


# deleta uma musica da tabela
def deletar(musica, id_playlist):
    playlist_atual = session.execute("select * from playlist_atual where nome = '{0}' and id_playlist={1} "
                                     "allow filtering;".format(musica, id_playlist))
    for dados in playlist_atual:
        posicao = dados.posicao
        id_playlist = dados.id_playlist
        session.execute(
            "delete from playlist_atual where posicao = {0} and id_playlist = {1};".format(posicao, id_playlist))
        atualiza_versao(id_playlist, 'DEL({0}, pos = {1})'.format(musica, posicao))
    print_table()


# retorna a posicao de uma musica
def posicao(musica):
    playlist_atual = session.execute("select * from playlist_atual where nome = '{0}';".format(musica))
    for dados in playlist_atual:
        playlist = dados.id_playlist
        posicao = dados.posicao
        album = dados.album
        artista = dados.artista
        id_musica = dados.id_musica
        nome = dados.nome
    return [playlist, posicao, album, artista, id_musica, nome]


def troca(musica1, musica2, playlist):
    # insere na playlist_versionada as musicas que trocarão de lugar
    atualiza_versao(playlist, 'TROCA({0},{1})'.format(musica1, musica2))
    # salva todas as informações da primeira musica
    musica1 = posicao(musica1)
    # print(musica1[0], musica1[1], musica1[2], musica1[3], musica1[4], musica1[5])
    # deleta a primeira musica da tabela
    deletar(musica1[5], musica1[0])
    # salva todas as informações da segunda musica
    musica2 = posicao(musica2)
    # print(musica2[0], musica2[1], musica2[2], musica2[3], musica2[4], musica2[5])
    # deleta a segunda musica
    deletar(musica2[5], musica2[0])
    # insere novamente a primeira musica, trocando o valor da posicao pelo valor da segunda
    session.execute("insert into playlist_atual(id_playlist, posicao, album, artista, id_musica, nome)"
                    "values ({0}, {1}, '{2}', '{3}', {4}, '{5}')".format
                    (musica1[0], musica2[1], musica1[2], musica1[3], musica1[4], musica1[5]))
    # atualiza a tabela de versao, com a nova posicao
    atualiza_versao(playlist, 'ADI({0}, pos = {1})'.format(musica1[5], musica2[1]))
    # insere novamente a segunda musica, trocando o valor da posicao pelo valor da primeira
    session.execute("insert into playlist_atual(id_playlist, posicao, album, artista, id_musica, nome)"
                    "values ({0}, {1}, '{2}', '{3}', {4}, '{5}')".format
                    (musica2[0], musica1[1], musica2[2], musica2[3], musica2[4], musica2[5]))
    # atualiza a tabela de versao, com a nova posicao
    atualiza_versao(playlist, 'ADI({0}, pos = {1})'.format(musica2[5], musica1[1]))


# testes

# limpa as tabelas
clean()
# insere as 4 musicas na tabela
insere_todas()
""" prompt insere_todas() 
1 1 Help! Beatles 6c0bdff2-cd46-4ad1-b107-40d2e8a84880 Help!
1 2 The Beatles Beatles 3c00fecc-f6cf-4601-9d11-a1be83f609cc Blackbird
1 3 Abbey Road Beatles 17ade43c-5296-4d87-9b55-b6e80bbe4e63 Something
1 4 Help! Beatles 8f6afe4a-c964-411e-a874-1ee89789c260 Yesterday
"""
deletar('Help!', 1)
print_table()
""" prompt deletar('Help!', 1)
1 2 The Beatles Beatles 3c00fecc-f6cf-4601-9d11-a1be83f609cc Blackbird
1 3 Abbey Road Beatles 17ade43c-5296-4d87-9b55-b6e80bbe4e63 Something
1 4 Help! Beatles 8f6afe4a-c964-411e-a874-1ee89789c260 Yesterday
"""
troca('Blackbird', 'Something', 1)
print_table()
""" prompt troca('Blackbird', 'Something', 1)
1 2 Abbey Road Beatles 17ade43c-5296-4d87-9b55-b6e80bbe4e63 Something
1 3 The Beatles Beatles 3c00fecc-f6cf-4601-9d11-a1be83f609cc Blackbird
1 4 Help! Beatles 8f6afe4a-c964-411e-a874-1ee89789c260 Yesterday
"""
adicionar('Help!', 1)
print_table()
"""prompt adicionar('Help!', 1)
1 2 Abbey Road Beatles 17ade43c-5296-4d87-9b55-b6e80bbe4e63 Something
1 3 The Beatles Beatles 3c00fecc-f6cf-4601-9d11-a1be83f609cc Blackbird
1 4 Help! Beatles 8f6afe4a-c964-411e-a874-1ee89789c260 Yesterday
1 5 Help! Beatles 6c0bdff2-cd46-4ad1-b107-40d2e8a84880 Help!
"""

""" Comportamento da tabela de versionamento
id_playlist | versao | modificacao
-------------+--------+----------------------------
           1 |      1 |                 ADI(Help!)
           1 |      2 |             ADI(Blackbird)
           1 |      3 |             ADI(Something)
           1 |      4 |             ADI(Yesterday)
           1 |      5 |        DEL(Help!, pos = 1)
           1 |      6 | TROCA(Blackbird,Something)
           1 |      7 |    DEL(Blackbird, pos = 2)
           1 |      8 |    DEL(Something, pos = 3)
           1 |      9 |    ADI(Blackbird, pos = 3)
           1 |     10 |    ADI(Something, pos = 2)
           1 |     11 |                 ADI(Help!)
"""
