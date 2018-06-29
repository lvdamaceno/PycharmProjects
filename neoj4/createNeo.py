from neo4jrestclient.client import GraphDatabase
# conecta ao banco
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123456")


user = db.labels.create("Usuario")

# cria os nós
u1 = db.nodes.create(name="Bob")
u2 = db.nodes.create(name="Alice")
u3 = db.nodes.create(name="Lea")
u4 = db.nodes.create(name="Ana")
u5 = db.nodes.create(name="Joel")

# adiciona os nós
user.add(u1, u2, u3, u4, u5)

# cria as arestas entre os nós, um tipo de rede social onde as pessoas se seguem
u1.relationships.create("follows", u2)
u4.relationships.create("follows", u1)
u2.relationships.create("follows", u3)
u2.relationships.create("follows", u5)