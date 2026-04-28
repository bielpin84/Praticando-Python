# Importando MongoCliente da biblioteca pymongo
from pymongo import MongoClient

# Definindo o MongoCliente e o endereço da conexão com o banco de dados
client = MongoClient("mongodb://localhost:27017/")

# Criando o banco de dados "escola" e a coleção "estudantes"
db = client["escola"]
estudantes = db["estudantes"]

# Inserindo uma enrtada na chave estudante
estudantes.insert_one({"nome": "João", "idade": 20})

# Iterando na chave estudantes para imprimir na tela
for estudante in estudantes.find():
    print(estudante)