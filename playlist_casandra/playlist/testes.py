# conexão com o banco
from cassandra.cluster import Cluster

cluster = Cluster()
# criar o banco antes
session = cluster.connect('aula')

def print_table():
    playlist = session.execute("select * from playlist_atual;")
    for musicas in playlist:
        print(musicas.id_playlist, musicas.posicao, musicas.album, musicas.artista, musicas. id_musica, musicas.nome)

def adicionar(nova_musica, id_lista):
    musica = nova_musica
    # verifica a ultima posicao na playlist, se for zero começa do 1
    # se for mair que 1 vai iterando
    # utlizando o codigo da id da playlist a função filtra antes de começar tudo para que numeração de posicao
    # seja diferente para cada playlist
    playlist_atual = session.execute("select * from playlist_atual where id_playlist={0} allow filtering".format(id_lista))
    # se o retorno da linha abaixo for uma lista vazia ele considera que nao exitem
    # registro na tabela, entao saré o primeiro
    if not playlist_atual.current_rows:
        posicao_atual = 0
        # print(posicao_atual)
    else:
        for dados in playlist_atual:
            pos = session.execute("select max(posicao) from playlist_atual where id_playlist={0} allow filtering".format(id_lista))
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
    print_table()

print_table()

