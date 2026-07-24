import json
animais = {"001":
    {"nome": "Cachorro",
    "especie": "Canide",
    "idade": 12
    },
}

with open("animais.json", "w") as arquivo:
    json.dump(animais, arquivo, indent=4)

def cadastrar_animal():
    #Captura o código do animal
    cod_animal = input("Digite o CÓDIGO do Animal: ")
    #Cria um discionário para os dados do animal
    novo_animal = {}
    novo_animal["nome"] = input("Digite o nome do animal: ")
    novo_animal["especie"] = input("Digite a espécie do animal: ")
    novo_animal["idade"] = float(input("Digite a idade do animal: "))

    animais.append(novo_animal)

    #Associa o CÓDIGO aos dados do animal no banco global
    animais[cod_animal] = novo_animal
    print(f"Animal {novo_animal['nome']} cadastrado com sucesso!")

def listar_animal():
    if not animais:
        print("Nenhum animal cadastrado")
        return
    
    print("\nLista de animais: ")
    for cod, dados in animais.items():
        print(f"""CÓDIGO: {cod},
    Nome: {dados['nome']},
    Especie: {dados['especie']},
    Idade: {dados['idade']}\n""")

def buscar_animal(cod_busca):
    if cod_busca in animais:
        dados = animais[cod_busca]
        print(f"Animal encontrado: {dados['nome']}")
        return dados
    else:
        print("Animal não encontrado.")
        return False


def ler_animais_json():
    with open("animais_cadastrados.json", "w") as arquivo:
    dados = json.load(arquivo)
    animais = dados

def escrever_animais_json():
    with open("animais.json", "w") as arquivo:
        json.dump(animais, arquivo, indent=4)

while True:
    print("\nSistema de gerenciamento dos animais")
    print("1. Cadastrar animal")
    print("2. Listar animal")
    print("3. Buscar animal")
    print("4. Atualizar animal")
    print("5. Excluir animal")
    print("0. Sair")

    if opcao == "1":
        cadastrar_animal()
    elif opcao == "2":
        listar_animal()
    elif opcao == "3":
        buscar_animal()
