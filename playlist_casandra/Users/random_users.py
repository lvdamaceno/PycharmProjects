# código para criar uma base randomica povoada
# names é um modulo com 40 nomes randomicos

import names
import random
# conexão com o banco
from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('aula')


# utilities


def create_table():
    # dropa a tabela
    session.execute("""drop table users""")

    # cria a tabela novamente sem dados
    session.execute(
        """
        CREATE TABLE users (
            id uuid PRIMARY KEY,
            lastname text,
            age text,
            city text,
            email text,
            firstname text);
        """
    )


# insere as linhas
def generate(qtd):
    # limpa a tabela
    create_table()
    pessoas = qtd
    for pessoa in range(pessoas):
        # insere os usuarios de teste
        idade = random.randint(10, 99)
        cidade = random.randint(111111, 999999)
        session.execute("""
        INSERT INTO users (id, lastname, age, city, email, firstname)
        VALUES (uuid(), '{0}', '{1}', '{2}', '{0}@gmail.com', '{3}');
        """.format(names.get_last_name(), idade, cidade, names.get_first_name()))


# seleciona as linhas do banco
def select_all():
    # executa os selects de teste
    users = session.execute("select * from users")
    print(
        # firula pra criar um cabeçalho pra tabela
        "First Name" + " " * 4 + "Last Name" + " " * 5 + "Age" + " " * 2 + "Cidade" + " " * 3 + "Email" + " " * 21 + "Id")
    print("-" * 104)
    for user in users:
        # ljust insere os espaços à esquerda
        print(user.firstname.ljust(13), user.lastname.ljust(13),
              user.age.ljust(4), user.city.ljust(8), user.email.lower().ljust(25),
              user.id)


# edita uma linha filtrando pelo ultimo nome, informando a coluna que será modificada e o novo valor
def edit(last_name, coluna, valor):
    pessoa = session.execute("select * from users where lastname='{0}' allow filtering".format(last_name))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set {1} = '{2}' where id = {0}".format(id, coluna, valor))
