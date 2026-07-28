import sqlite3

conexao = sqlite3.connect('ing.db')

cursor = conexao.cursor()

##Tabela de INGREDIENTES

# cursor.execute('''
# CREATE TABLE INGREDIENTES (
#     ID INTEGER PRIMARY KEY,
#     Ingredientes TEXT,
#     Usado INTEGER,
#     Preço REAL,
#     Compra TEXT,
#     Unidade TEXT
# )
# ''')

# conexao.commit()

# # Tabela de RECEITAS

# cursor.execute('''
# CREATE TABLE RECEITAS (
#     ID INTEGER PRIMARY KEY,
#     Produto TEXT,
#     Preço REAL,
#     Unidades INTEGER
# )
# ''')

# conexao.commit()

def inserir_dados(ingredientes, usado, preco, compra, unidade):
    cursor.execute('''
    INSERT INTO INGREDIENTES (Ingredientes, Usado, Preço, Compra, Unidade)
    VALUES (?, ?, ?, ?, ?)''', (ingredientes, usado, preco, compra, unidade))

    conexao.commit()

ingredientes = input("Insira o ingrediente: ")
usado = int(input("Quantidade usada: "))
preco = float(input("Digite o preço do ingrediente: "))
compra = int(input("Quantidade do ingrediente comprado: "))
unidade = input("Unidade de medida: ")
inserir_dados(ingredientes, usado, preco, compra, unidade)