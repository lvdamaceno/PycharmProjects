from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

# conecta ao banco
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123456")

# consulta no banco
q = 'MATCH (u1:Usuario)-[r:follows]->(u2:Usuario) WHERE u1.name="Alice" RETURN u1, type(r), u2'

# passa a consulta escrita em cypher com a variavel q, e tras o resultado que é um nó, uma string e outro nó
# como foi seleciondo na consulta feita em q
result = db.query(q, returns=(client.Node, str, client.Node))

# se uma pessoa pode seguir mais de outra pessoa é necessario um laço iterador
for r in result:
    # r[0] é o primeiro nó, e precisamos do atributo name, assim como o  r[2], r[1] é o tipo
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))