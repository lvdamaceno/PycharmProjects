# testes iniciais com o cassandra
def connection():
    from cassandra.cluster import Cluster
    cluster = Cluster()
    session = cluster.connect('aula')
    return session


cassandra = connection()

# dropa a tabela usuarios para evitar inserir dados que já existem
cassandra.execute("""drop table users""")

# cria a tabela novamente sem dados
cassandra.execute(
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

# insere os usuarios de teste
cassandra.execute("""
INSERT INTO users (id, lastname, age, city, email, firstname)
VALUES (uuid(), 'Jones', '35', 'Austin', 'bob@example.com', 'Bob');
""")

cassandra.execute("""
INSERT INTO users (id, lastname, age, city, email, firstname)
VALUES (uuid(), 'Brown', '27', 'Berlim', 'george@example.com', 'George');
""")

cassandra.execute("""
INSERT INTO users (id, lastname, age, city, email, firstname)
VALUES (uuid(), 'Scott', '18', 'Mexico', 'millie@example.com', 'Millie');
""")

cassandra.execute("""
INSERT INTO users (id, lastname, age, city, email, firstname)
VALUES (uuid(), 'Varley', '41', 'United States', 'lynn@example.com', 'Lynn');
""")

# executa os selects de teste

qtd_linhas = cassandra.execute("""
select count(id) as qtd from users;
""")

result = cassandra.execute("select * from users")
for user in result:
    print(user.age, user.lastname)


