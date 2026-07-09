"""Questão 3: Escreva uma função chamada contar_vogais que receba uma string e retorne o número de vogais (a, e, i, o,
u) na string."""

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    count = 0
    for char in texto:  #char é apenas o nome da variavel. char(caractere)
        if char in vogais:
            count += 1
    return count
    
texto = input("Digite um texto: ")
print("Número de vogais: ", contar_vogais(texto))
