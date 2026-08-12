import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('ficha_tecnica.db')
cursor = conexao.cursor()

#Cores Padrao
COR_FUNDO = "#fef3e8"
COR_TEXTO = "#000000"
COR_BOTAO = "#743808"
COR_BOTAO_TEXTO = "#F7F2F2"
COR_BOTAO_2 = "#e9dcce"

# criando janela
janela = tk.Tk()
janela.title("Ficha Técnica")
janela.geometry("800x800+100+100")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

janela2 = tk.Tk()
janela2.title("Ficha Técnica")
janela2.geometry("800x800+100+100")
janela2.configure(bg=COR_FUNDO)
janela2.resizable(False, False)

# criando frame
frame = tk.Frame(janela)
# label = tk.Label(janela, text="Procurar Por",   bg=COR_FUNDO)
# label.pack(padx=20, pady=5)


label1 = tk.Label(janela, text="Ficha Técnica de Preparo", bg= COR_FUNDO)
label1.pack()
label1.pack(padx= 100, pady= 5)

label2 = tk.Label(janela2, text="Ficha Técnica de Preparo", bg= COR_FUNDO)
label2.pack()
label2.pack(padx= 100, pady= 5)


janela.mainloop()

# Tabela da ficha técnica
cursor.execute('''CREATE TABLE IF NOT EXISTS Ficha_Tecnica(
        ID INTEGER PRIMARY KEY,
        Ingredientes TEXT NOT NULL,
        Qunt_Comprada INTEGER,
        Valor_Comprado REAL,
        Qunt_Usada INTEGER,
        Unid_Medida TEXT,
        Valor_Usado REAL)
        ''')

# Tabela do modo de preparo
cursor.execute('''CREATE TABLE IF NOT EXISTS Preparo(
        ID INTEGER PRIMARY KEY,
        ingrediente TEXT NOT NULL,
        modo_de_preparo TEXT NOT NULL)
        ''')

conexao.commit()

def mostrar_menu():
    pass

def limpar_tabela():
    pass

def buscar_dados():
    pass


# Inserir os dados na tabela de igredientes

def cadastrar_ing():
    print("Cadastrar Ingrediente")
    nome_ingrediente = campo_nome.get()
    quantidade_comprada = campo_qunt.get()
    valor_comprado = campo_valor_comp.get()
    quant_usada = campo_qunt_usada.get()
    unidade = campo_unidade.get()
    valor_usado = campo_valor_usado.get()

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
    pass