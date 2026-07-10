"""Questão 1: Crie um dicionário que represente informações sobre uma pessoa, como nome, idade, cidade natal e
profissão."""
pessoa = {"nome": "João",
              "idade": 20,
              "cidade": "Fortaleza",
              "profissão": "Programação"}

for chave in pessoa:
    print(f"{pessoa[chave]}")
