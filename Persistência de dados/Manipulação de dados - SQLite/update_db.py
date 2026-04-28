# 1 Importando a biblioteca do SQLite
import sqlite3

# 2 Conectando com o banco de dados
conn = sqlite3.connect("./Manipulação de dados - SQLite/escola.db")

# 3 Criando uma forma de executar comandos no banco de dados com o cursor
cursor = conn.cursor()

# 4 Usando o execute para recuperar/consultar os dados das tabelas do banco de dados
cursor.execute(
    """
        UPDATE estudantes SET nome = ? WHERE \
        id = ?
    """,
    ("Leandro", 2)
)

# 5 Confirmando as alterações
conn.commit()

# 6 Fechando a conexão com o banco de dados
conn.close()