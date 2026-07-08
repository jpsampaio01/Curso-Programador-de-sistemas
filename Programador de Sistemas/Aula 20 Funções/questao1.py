"""Questão 1: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma
desses três argumentos."""
def argumentos():
    while True:
        print("""Escolha uma opçao
            1 - soma
            2 - Multiplicação
            0 - sair""")
        opcao = input("Qual você quer?")

        if opcao == "1":
            n1, n2, n3 = numeros()
            soma(n1, n2, n3)
        elif opcao == "0":
            print("Saindo do programa...")
            break


def soma(a, b, c):
    resultado = a + b + c
    print(f"O resultado da soma é {soma}.")
    
def numeros():
    n1 = int(input("Numero: "))
    n2 = int(input("Numero: "))
    n3 = int(input("Numero: "))
    return n1, n2, n3

argumentos()