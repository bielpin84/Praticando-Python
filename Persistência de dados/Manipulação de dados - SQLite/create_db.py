# 1 Importando a biblioteca do SQLite
import sqlite3

# 2 Conectando com o banco de dados (caso não exista, cria o mesmo)
conn = sqlite3.connect("./Manipulação de dados - SQLite/escola.db")

# 3 Criando uma forma de executar comandos no banco de dados com o cursor
cursor = conn.cursor()

# 4 Usando o execute para criar as tabelas no banco de dados
# 4.1 Criando a tabela 'estudantes'
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
)

# 4.2 Criando a tabela 'disciplinas'
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS disciplinas(
            id INTEGER PRIMARY KEY,
            nome_disciplina TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) \
                REFERENCES estudantes(id)
        )
    """
)

# 5 Confirmando as alterações
conn.commit()

# 6 Fechando a conexão com o banco de dados
conn.close()