"""Questão 2 : Escreva uma função chamada calcular_media que receba uma lista de números e retorne a média desses
números."""
def media_lista(lista):
    return sum(lista) / len(lista)  #sum == soma / len == mostra a quantidade de numeros
lista = []
for i in range (4):
    numero = float(input("Digite um número: "))
    lista.append(numero)

print("A média dos números é:", media_lista(lista))