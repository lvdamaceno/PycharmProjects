# importa o pacote para conexão e trabalho com o mongo db
import pymongo

# faz a conexão com o banco local
client = pymongo.MongoClient("localhost", 27017)

# variavel db recebe os dados do banco aula através da conexão client
db = client.aula

# conselta dentro do banco as informações dos albuns e guarda na variavel
albuns = db.albuns.find()

# cria uma arquivo txt para receber os albuns, o a no final é de append
file = open("/home/puc/PycharmProjects/MongoDb/albuns.txt", "a")

# laço para percorrer os albuns e coletar os nomes dos albuns
for item in albuns:
    # o laço começa a percorrer documento à documento, nesse caso quando ele entra no documento x
    # vai procurar o elemento nome, importante todos os documentos terem 'nome' para nao dar erro
    # e ao final escreve o nome no arquivo criado, com uma quebra de linha ao final de cada um.
    nome = item["nome"]
    file.write(nome + '\n')


# fecha o arquivo
file.close()