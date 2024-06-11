# Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as 
# seguintes informações sobre alunos de uma disciplina, sendo todas as 
# informações do tipo inteiro:

# a. Primeira coluna: número de matrícula (use um inteiro)
# b. Segunda coluna: media das provas
# c. Terceira coluna: media dos trabalhos
# d. Quarta coluna: nota final

# Elabore um programa que:

# a. Leia as três primeiras informações de cada aluno;
# b. Calcule a nota final como sendo a soma da média das provas e da 
# média dos trabalhos;
# c. Imprima a matrícula do aluno que obteve a maior nota final (assuma 
# que só existe uma maior nota).


matriz = [
    [4444, 5, 2, 0],  
    [5555, 3, 4, 0],  
    [6666, 2, 1, 0],  
    [7777, 4, 5, 0],  
    [8888, 1, 3, 0]   
]


for i in range(5):
    media_provas = matriz[i][1]
    media_trabalhos = matriz[i][2]
    nota_final = (media_provas + media_trabalhos) 
    matriz[i][3] = nota_final


print("\nMatriz de informações dos alunos:")
print("Matrícula | Média das Provas | Média dos Trabalhos | Nota Final")
for aluno in matriz:
    print(f"{aluno[0]:^9} | {aluno[1]:^16.2f} | {aluno[2]:^19.2f} | {aluno[3]:^10.2f}")
    # Abaixo, versão do print menos legal
    # print(aluno)


maior_nota_final = matriz[0][3]
matricula_maior_nota = matriz[0][0]

for aluno in matriz:
    if aluno[3] > maior_nota_final:
        maior_nota_final = aluno[3]
        matricula_maior_nota = aluno[0]


print(f"\nA matrícula do aluno com a maior nota final ({maior_nota_final:.2f}) é: {matricula_maior_nota}")
