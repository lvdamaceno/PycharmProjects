# código para criar uma base randomica povoada
# names é um modulo com 40 nomes randomicos

import names
import random
# conexão com o banco
from cassandra.cluster import Cluster

cluster = Cluster()
# criar o banco antes
session = cluster.connect('aula')


# funções de criação

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


# Funções de seleção

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


# Funções de edição

# edita uma linha inteira filtrando pelo ultimo nome, informando a coluna que será modificada e o novo valor
def edit(last_name, coluna, valor):
    pessoa = session.execute("select * from users where lastname='{0}' allow filtering".format(last_name))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set {1} = '{2}' where id = {0}".format(id, coluna, valor))
    print("")


# edita o valor da idade informado o id da pessoa e o novo valor
def edit_age(id, valor):
    pessoa = session.execute("select * from users where id={0} allow filtering".format(id))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set age = '{1}' where id = {0}".format(id, valor))
    select_all()
    print("")


# edita o ultimo nome informado o id da pessoa e a correção
def edit_first_name(id, firstname):
    pessoa = session.execute("select * from users where id={0} allow filtering".format(id))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set firstname = '{1}' where id = {0}".format(id, firstname))
    select_all()
    print("")


# edita o ultimo nome informado o id da pessoa e a correção
def edit_last_name(id, lastname):
    pessoa = session.execute("select * from users where id={0} allow filtering".format(id))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set lastname = '{1}' where id = {0}".format(id, lastname))
        session.execute("update users set email = '{1}@gmail.com' where id = {0}".format(id, lastname))
    select_all()
    print("")


# edita o nome inteiro informado o id da pessoa e a correção
def edit_all_name(id, nome):
    nome = nome.partition(" ")
    firstname = nome[0]
    lastname = nome[2]
    pessoa = session.execute("select * from users where id={0} allow filtering".format(id))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set firstname = '{1}' where id = {0}".format(id, firstname))
        session.execute("update users set lastname = '{1}' where id = {0}".format(id, lastname))
        session.execute("update users set email = '{1}@gmail.com' where id = {0}".format(id, lastname))
    select_all()
    print("")


# edita o email informado o id da pessoa e a correção
def edit_email(id, mail):
    pessoa = session.execute("select * from users where id={0} allow filtering".format(id))
    for dados in pessoa:
        id = dados.id
        session.execute("update users set email = '{1}' where id = {0}".format(id, mail))
    select_all()
    print("")
