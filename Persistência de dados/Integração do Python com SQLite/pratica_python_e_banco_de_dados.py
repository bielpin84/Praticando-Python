"""
A Loja TechMais está informatizando seu controle de estoque
O gerente quer um sistema simples em Python que registre e consulte produtos no banco de dados loja.db.

Se conecta ao banco loja.db;

Crie uma tabela produtos com os campos id, nome, preco;

Insira 3 produtos diferentes;

Liste todos os produtos cadastrados.

Dica: use funções como criar_produto(nome, preco) e listar_produtos().
"""
import sqlite3

conectar = lambda database: sqlite3.connect(database)

def criar_tabela(db, nome_tabela, parametros):
    conn = conectar(db)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela}({parametros})")
    conn.commit()
    conn.close()

def criar_produto(db, nome, preco):
    conn = conectar(db)
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO produtos (nome, preco) \
            VALUES (?, ?)
        """, (nome, preco)
    )
    conn.commit()
    conn.close()

def ler_tudo_da_tabela(db, nome_tabela):
    conn = conectar(db)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    dados = cursor.fetchall()
    conn.commit()
    conn.close()
    return dados
    
if __name__ == "__main__":
    caminho = "./Integração do Python com SQLite/loja.db"
    criar_tabela(caminho, "produtos", "id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL")
    criar_produto(caminho, "caderno", 7.95)
    criar_produto(caminho, "caneta bic azul", 3.20)
    criar_produto(caminho, "caneta bic vermelha", 3.70)
    produtos = ler_tudo_da_tabela(caminho, "produtos")
    print("Produtos:")
    for produto in produtos:
        print(f"Id: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}")