# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os 
# demais elementos. Escreva ao final a matriz obtida.

matriz = [[0] * 5 for _ in range(5)]

matriz[0][0] = 1
matriz[1][1] = 1
matriz[2][2] = 1
matriz[3][3] = 1
matriz[4][4] = 1

for i in matriz:
    print(i)