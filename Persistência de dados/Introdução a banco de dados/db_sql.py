# Importando a biblioteca do sqlite3
import sqlite3

# Criando uma conexão com o banco de dados, cria o banco de dados caso ele não exista
conn = sqlite3.connect("escola.db")

# Variável cursor para executar tarefas no banco de dados
cursor = conn.cursor()

# Execução de comando SQL para criar a tabela 'estudantes' caso não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

# Execução de comando SQL para inserir dados na tabela estudantes
cursor.execute(
    "INSERT INTO estudantes (nome, idade)\
    VALUES (?, ?)", ("João", 20))

# Execução do comando commit para salvar as alterações feitas no banco de dados
conn.commit()

# Recuperando os dados na tabela estudantes
cursor.execute("SELECT * FROM  estudantes")

# Imprimindo na tela o que foi recuperado da tabela
print(cursor.fetchall())

# Encerrando a conexão com o banco de dados
conn.close()