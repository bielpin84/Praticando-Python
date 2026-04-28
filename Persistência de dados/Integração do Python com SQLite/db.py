import sqlite3
caminho = "./Integração do Python com SQLite/escola.db"

# def conectar(database):
#     return sqlite3.connect(database)

conectar = lambda database: sqlite3.connect(database)

# def criar_tabela_estudantes():
#     conn = conectar(caminho)
#     cursor = conn.cursor()
#     cursor.execute(
#         """
#             CREATE TABLE IF NOT EXISTS estudantes(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT,
#                 idade INTEGER
#             )
#         """
#     )

def criar_tabela(nome_tabela, parametros):
    conn = conectar(caminho)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela}({parametros})")
    conn.commit()
    conn.close()

def criar_estudante(nome, idade):
    conn = conectar(caminho)
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO estudantes (nome, idade) \
            VALUES (?, ?)
        """, (nome, idade)
    )
    conn.commit()
    conn.close()

def criar_matricula(estudante_id, nome_disciplina):
    conn = conectar(caminho)
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO matriculas (estudante_id, nome_disciplina) \
            VALUES(?, ?)
        """, (estudante_id, nome_disciplina)
    )
    conn.commit()
    conn.close()

def ler_da_tabela(nome_tabela):
    conn = conectar(caminho)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    dados = cursor.fetchall()
    conn.commit()
    conn.close()
    return dados

def listar_matriculas():
    conn = conectar(caminho)
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT matriculas.id, estudantes.nome, matriculas.nome_disciplina FROM matriculas
            JOIN estudantes ON matriculas.estudante_id = estudantes.id
        """
    )
    dados = cursor.fetchall()
    print("Matrículas:")
    for dado in dados:
        print(f"Id: {dado[0]}, Nome Estudante: {dado[1]}, Nome Disciplina: {dado[2]}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabela("estudantes", "id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER")

    criar_tabela("matriculas", "id INTEGER PRIMARY KEY AUTOINCREMENT, nome_disciplina TEXT, estudante_id INTEGER, FOREIGN KEY (estudante_id) REFERENCES estudantes(id)")

    criar_estudante("Luana", 20)
    criar_estudante("Lucas", 22)

    criar_matricula(1, "Matemática")
    criar_matricula(2, "Português")
    
    estudantes = ler_da_tabela("estudantes")
    for estudante in estudantes:
        print(f"Id: {estudante[0]}, Nome: {estudante[1]}, Idade: {estudante[2]}")

    matriculas = ler_da_tabela("matriculas")
    for matricula in matriculas:
        print(f"Id: {matricula[0]}, Disciplina: {matricula[1]}, Id Estudante: {matricula[2]}")
    
    listar_matriculas()