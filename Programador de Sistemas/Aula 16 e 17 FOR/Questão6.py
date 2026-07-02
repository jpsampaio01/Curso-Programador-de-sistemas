"""Somando Apenas Números Pares: Escreva um programa em Python que utilize um loop for para
calcular a soma de todos os números pares de 1 a 50."""

soma_par = 0
soma_impar = 0
for i in range(1, 51):
    if i % 2 == 0:
        soma_par += i
    if i % 2 != 0:
        soma_impar += i

print(f"A soma de todos os números pares de 1 a 50 é {soma_par} e impares é {soma_impar}")
