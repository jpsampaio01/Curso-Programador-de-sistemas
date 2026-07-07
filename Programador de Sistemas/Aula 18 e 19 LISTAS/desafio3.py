"""Lista de Convidados - Você foi contratado para desenvolver um sistema simples para controlar a lista de convidados de uma festa.
Crie um programa com o seguinte menu: 
========== MENU ==========
1 - Adicionar convidado
2 - Listar convidados 
3 - Consultar convidado
4 - Remover convidado
5 - Quantidade de convidados
6 - Editar Convidado
0 - Finalizar programa
Regra: O programa somente deverá ser encerrado quando o usuário escolher a opção 0."""

convidados = []

while True:
    print("""=============== Menu ===============
          1 - Adicionar Convidado
          2 - Listar Convidados
          3 - Consultar Convidados
          4 - Remover Convidado
          5 - Quantidade de Convidados
          6 - Editar Convidado
          0 - Sair\n""")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        while True:
            nome = input("Digite o nome do convidado (ou 'sair' para voltar ao menu): ")
            if nome.lower().replace(" ","") == 'sair':
                break
            elif nome in convidados:
                print(f"{nome} já está na lista de convidados.\n")
            else:
                convidados.append(nome)
                print(f"{nome} adicionado à lista de convidados.\n")

    elif opcao == 2:
        print("Lista de convidados: ")
        for convidado in convidados:
            print(convidado)
        print()

    elif opcao == 3:
        nome = input("Digite o nome do convidado a ser consultado: ")
        if nome in convidados:
            print(f"{nome} está na lista de convidados\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")

    elif opcao == 4:
        nome = input("Digite o nome do convidado a ser removido: ")
        if nome in convidados:
            convidados.remove(nome)
            print(f"{nome} removido da lista de convidados.\n")
        else:
            print(f"{nome} não está na lista de convidados.\n")

    elif opcao == 5:
        print(f"Quantidade de convidados: {len(convidados)}\n")

    elif opcao == 6:
        nome_antigo = input("Digite o nome do convidado a ser editado: ")
        if nome_antigo in convidados:
            nome_novo = input("Digite o novo nome do convidado: ")
            index = convidados.index(nome_antigo)
            convidados[index] = nome_novo
            print(f"{nome_antigo} foi atualizado para {nome_novo}.\n")
        else:
            print(f"{nome_antigo} não está na lista de convidados.\n")

    elif opcao == 0:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")