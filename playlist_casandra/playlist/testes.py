# conexão com o banco
from cassandra.cluster import Cluster
from playlist import playlists

cluster = Cluster()
# criar o banco antes
session = cluster.connect('aula')

def troca(musica1, musica2):
    musica1 = posicao(musica1)
    m1_playlist = musica1[0]
    m1_posicao = musica1[1]
    m1_musica = musica1[2]
    print(m1_playlist, m1_posicao, m1_musica)

    musica2 = posicao(musica2)
    m2_playlist = musica2[0]
    m2_posicao = musica2[1]
    m2_musica = musica2[2]
    print(m2_playlist, m2_posicao, m2_musica)