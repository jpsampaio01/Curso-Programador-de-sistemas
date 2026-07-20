"""Faça um programa que receba do usuario um arquivo texto. Crie outro arquivo texto ´ contendo o texto do arquivo de
entrada, mas com as vogais substituídas por ‘*’."""

def subistituir_caracter_arquivo():
    nome_arquivo = input("Digite o nome do arquivo: ")
    vogais = "aeiouAEIOU"
    novo_texto = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            for caractere in conteudo:
                novo_texto.append("*")
            else:
                novo_texto.append(caractere)
    with open("novo_texto_substituido.txt", 'w', encoding='utf-8') as arquivo:
        arquivo.write(''.join(novo_texto))
        print("Novo arquivo criado com sucesso!")
except FileNotFoundError
    print("Erro: ")