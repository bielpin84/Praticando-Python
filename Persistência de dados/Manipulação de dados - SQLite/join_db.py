# 1 Importando a biblioteca do SQLite
import sqlite3

# 2 Conectando com o banco de dados
conn = sqlite3.connect("./Manipulação de dados - SQLite/escola.db")

# 3 Criando uma forma de executar comandos no banco de dados com o cursor
cursor = conn.cursor()

# 4.1 Consultando os dados da tabela estudantes com o JOIN
cursor.execute(
    """
        SELECT estudantes.nome, disciplinas.nome_disciplina FROM disciplinas JOIN estudantes ON disciplinas.estudante_id
    """
)

# 5 Confirmando as alterações
conn.commit()

# 6 Usando o comando fetchall() para ler os dados e salvar em uma váriavel
estudantes = cursor.fetchall()

# 7 Iterando e printando os elementos da variável onde os dados foram salvos
for estudante in estudantes:
    print(estudante)

# 8 Fechando a conexão com o banco de dados
conn.close()