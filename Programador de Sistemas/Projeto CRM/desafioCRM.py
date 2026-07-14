clientes = {"12345678901": {"nome": "Joao Paulo", "idade": 20, "compras": [110.50, 79.90, 50.00], "categoria": "Regular"},
            "98765432100": {"nome": "Sandro Freire", "idade": 35, "compras": [350.00, 500.00], "categoria": "Regular"},
            "45678912344": {"nome": "Jessica Silva", "idade":19, "compras":[50.00], "categoria": "Regular"},
            "78912345655": {"nome": "Alana Maria", "idade": 21, "compras": [15.00, 30.00, 25.50, 40.00], "categoria": "Regular"}
}



def cadastrar_cliente():
    #Captura o CPF para usar como chave principal
    cpf_chave = input("Digite o CPF do cliente: ")
    #Cria um discionário para os dados do cliente
    novo_cliente = {}
    novo_cliente["nome"] = input("Digite o nome do cliente: ")
    novo_cliente["idade"] = int(input("Digite a lista do cliente: "))
    novo_cliente["compras"] = []
    novo_cliente["categoria"] = "Regular"
    
    clientes[cpf_chave] = novo_cliente
    print(f"Cliente {novo_cliente['nome']} cadastrado com sucesso!")
    
def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\nLista de clientes:")
    for cpf, dados in clientes.items():
        print(f"""CPF: {cpf},
    Nome: {dados['nome']}
    Idade: {dados['idade']},
    Categoria: {dados['categoria']},
    Compras: {dados['compras']}\n""")
              
def buscar_cliente(cpf_busca):
    pass
def atualizar_cliente():
    pass
def excluir_cliente():
    pass


