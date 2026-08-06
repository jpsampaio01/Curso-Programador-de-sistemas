import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('ficha_tecnica.db')
cursor = conexao.cursor()

# Tabela da ficha técnica
cursor.execute('''CREATE TABLE IF NOT EXISTS Ficha_Tecnica(
        ID INTEGER PRIMARY KEY,
        Ingredientes TEXT NOT NULL,
        Quantidade_Comprada INTEGER,
        Preco_Comprado REAL,
        Quantidade_Usada INTEGER,
        Unidade TEXT,
        Preco_gasto REAL)
        ''')

# Tabela ingredientes
cursor.execute('''CREATE TABLE IF NOT EXISTS ingredientes(
        ID INTEGER PRIMARY KEY,
        nome_ingrediente TEXT NOT NULL)
        ''')

# Tabela produtos
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos(
        ID INTEGER PRIMARY KEY,
        nome_produto TEXT NOT NULL)
        ''')

conexao.commit()

# Variáveis globais para texto nas telas
entry_usuario = None
entry_senha = None
entry_usuario_cadastro = None
entry_senha_cadastro = None
entry_senha_confirmar = None

#Cores Padrao
COR_FUNDO = "#3F3C3C"
COR_TEXTO = "#FFFFFF"
COR_BOTAO = "#7FC7F7"
COR_BOTAO_TEXTO = "#F7F2F2"
COR_BOTAO_2 = "#7cfad4"

def mostrar_menu():
    pass

def limpar_tabela():
    pass

def buscar_dados():
    pass


# Inserir os dados na tabela de igredientes

def cadastrar_ing():
    pass

def listar_ing():
    pass

def buscar_ing():
    pass

def atualizar_ing():
    pass

def excluir_ing():
    pass

# ____________________________ INTERFACE ________________________ #

def tela_ingredientes():

    # criando janela
    janela = tk.Tk()
    janela.title("Ficha Técnica")
    janela.geometry("900x900")
    janela.resizable(False, False)

    # criando frame
    frame = tk.Frame(janela)

    # label 1
    label1 = tk.Label(janela, text="Ficha Técnica")
    label1.pack()

    janela.mainloop()