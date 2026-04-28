# 1 Importando a biblioteca do SQLite
import sqlite3

# 2 Conectando com o banco de dados
conn = sqlite3.connect("./Manipulação de dados - SQLite/escola.db")

# 3 Criando uma forma de executar comandos no banco de dados com o cursor
cursor = conn.cursor()

# 4 Usando o execute para inserir dados nas tabelas do banco de dados

# 4.1 Inserindo dados na tabela de estudantes
# cursor.execute(
#     """
#         INSERT INTO estudantes(nome, idade) \
#         VALUES (?, ?)
#     """,
#     ("Joana", 19)
# )

# 4.2 Inserindo dados na tabela de disciplinas
cursor.execute(
    """
        INSERT INTO disciplinas(
        estudante_id, nome_disciplina
        ) VALUES (?, ?)
    """,
    (1, "Matemática")
)

# 5 Confirmando as alterações
conn.commit()

# 6 Fechando a conexão com o banco de dados
conn.close()