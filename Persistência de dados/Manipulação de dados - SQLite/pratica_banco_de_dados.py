"""
A rede de hotelaria HotelPlus te contratou para criar um pequeno sistema de cadastro de usuários. A priori você precisa criar uma tabela chamada usuarios com os seguintes campos:

id (inteiro, chave primária)

nome (texto)

email (texto)

Para testar o seu banco de dados, adicione 2 usuários na tabela usuarios e depois consulte todos os registros.
"""
import sqlite3

def criar_tabela():
    conn = sqlite3.connect("./Manipulação de dados - SQLite/hotelplus.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT
            )
        """
    )
    conn.commit()
    conn.close()

def inserir_dados(nome, email):
    conn = sqlite3.connect("./Manipulação de dados - SQLite/hotelplus.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO usuarios(
            nome, email
            ) VALUES (?, ?)
        """,
        (nome, email)
    )
    conn.commit()
    conn.close()

def ler_dados():
    conn = sqlite3.connect("./Manipulação de dados - SQLite/hotelplus.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM usuarios
        """
    )
    conn.commit()
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

if __name__ == "__main__":
    criar_tabela()
    inserir_dados("Maria", "maria@email.com.br")
    inserir_dados("João", "joao@email.com.br")
    usuarios = ler_dados()
    for usuario in usuarios:
        print(usuario)

