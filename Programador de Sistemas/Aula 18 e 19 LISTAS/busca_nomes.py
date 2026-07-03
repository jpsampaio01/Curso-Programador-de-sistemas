"""Faça um programa que crie uma lista de 10 clientes e preenche os nomes
desses 10 clientes dentro de um laço de repetição.(Dê ua mensagem de bom dia! Para cada cliente)"""

cliente = []
for i in range(9):
    nome = input('Digite o nome do cliente: ')
    cliente.append(nome)

print(f"Bom dia! {cliente}")