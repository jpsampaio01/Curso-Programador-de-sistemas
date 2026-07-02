"""Escreva um programa em Python que utilize um loop for para imprimir todos os números ímpares 
de 1 a b 20."""

#Modo fácil, mais situacional.
for i in range(1, 20, 2):
    print(i)

#Modo dificil mas funciona em qualquer situação.
for i in range(21):
    if i % 2 != 0:
        print(i)
