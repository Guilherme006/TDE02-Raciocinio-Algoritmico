# Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a 
# coluna) do maior valor.


import random


matriz = [[random.randint(1,100) for _ in range(4)] for _ in range(4)]

maior = matriz[0][0]

linha_maior = 0
coluna_maior = 0


for linha in range(4):
    for coluna in range(4):
        if matriz[linha][coluna] > maior:
            linha_maior = linha
            coluna_maior = coluna

for i in matriz:
    print(i)

print(f"\nO maior número está na linha {linha_maior + 1} e na coluna {coluna_maior + 1}")