# Crie uma função chamada maior_elemento que receba uma lista de números 
# como parâmetro e retorne o maior elemento dessa lista.

import random

def maior_elemento(lista):
    maior = lista[0]
    
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    
    return maior


lista = [random.randint(1, 100) for _ in range(10)]


resultado = maior_elemento(lista)
print(f"A lista é: {lista}")
print(f"O maior número da lista é {resultado}")

# def maior_elemento():
    
#     lista = [random.randint(1, 100) for _ in range(10)]

#     maior = lista[0]
    
#     for numero in lista:
#         if numero > maior:
#             maior = numero
    
#     print(f"A lista é: {lista}")
#     print(f"O maior número da lista é {maior}")


# maior_elemento()