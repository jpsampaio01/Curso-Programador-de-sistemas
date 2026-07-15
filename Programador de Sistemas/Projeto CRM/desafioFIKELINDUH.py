clientes = {"12345678901": 
            {"nome": "Joao Paulo", 
            "idade": 20, 
            "compras": [110.50, 79.90, 50.00], 
            "categoria": "Regular"
            },

            "98765432100": 
            {"nome": "Sandro Freire", 
             "idade": 35, 
             "compras": [350.00, 500.00], 
             "categoria": "Regular"
             },

            "45678912344": 
            {"nome": "Jessica Silva", 
             "idade":19, 
             "compras":[50.00], 
             "categoria": "Regular"
             },

            "78912345655": 
            {"nome": "Alana Maria", 
             "idade": 21, 
             "compras": [15.00, 30.00, 25.50, 40.00], 
             "categoria": "Regular"
             }
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
    #Associa o CPF aos Dados do Cliente no banco global
    clientes[cpf_chave] = novo_cliente
    print(f"Cliente {novo_cliente['nome']} cadastrado com sucesso!")
    
def listar_cliente():
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
    if cpf_busca in clientes:
        dados = clientes[cpf_busca]
        print(f"Cliente encontrado: {dados['nome']}")
        return dados
    else:
        print("Cliente não encocntrado.")
        return False
    
def atualizar_cliente():
    cpf_atualizar = input("Digite o CPF do cliente que deseja Atualizar: ")
    cliente = buscar_cliente(cpf_atualizar)
    if cliente:
        cliente["nome"] = input("Digite o nome do cliente: ")
        cliente["idade"] = int(input("Digite a idade do cliente: "))
        print(f"Cliente {cliente['nome']} atualizado com sucesso!")

def excluir_cliente():
    cpf_deletar = input("Digite o CPF do cliente que deseja deletar: ")
    clientes = buscar_cliente(cpf_deletar)
    if clientes:
    del clientes[cpf_deletar]
    print("Cliente excluido com sucesso")

def calcular_fatura():
    cpf_cliente = input("Digite o CPF do cliente que deseje fazer a compra: ")
    cliente = buscar_cliente(cpf_cliente)
    if cliente:
        faturamento = sum(cliente["compras"])
        print(f"faturamento total do cliente {cliente["nome"]} é R$ {faturamento:.2f}")

def fazer_compra():
    cpf_cliente = input("Digite o CPF do cliente que deseja fazer a compra: ")
    cliente_compra = buscar_cliente(cpf_cliente)

    if cliente_compra:
        valor_compra = float(input("Digite o valor da Compra: "))
        cliente_compra["compras"].append(valor_compra)

while True:
    print("\nSistema de Gerenciamento de Clientes FIKELINDUH")
    print("1. Cadastrar cliente")
    print("2. Listar cliente")
    print("3. Buscar cliente")
    print("4. Atualizar cliente")
    print("5. Excluir cliente")
    print("6. Fazer compra")
    print("7. Faturamento cliente")
    print("0. Sair")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_cliente()
    elif opcao == "3":
        buscar_cliente()
    elif opcao == "4":
        atualizar_cliente()
    elif opcao == "5":
        excluir_cliente()
    elif opcao == "6":
        fazer_compra()
    elif opcao == "7":
        calcular_fatura()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente...")
