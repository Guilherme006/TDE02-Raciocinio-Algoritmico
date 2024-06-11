# Crie uma função chamada soma_elementos que receba uma lista de números 
# como parâmetro e retorne a soma de todos os elementos dessa lista.

import random

lista = [random.randint(1,100) for _ in range(10)]

def soma_elementos(lista):
    return sum(lista)

resultado = soma_elementos(lista)
print(f"A lista é: {lista}")
print(f"A soma dos elementos da lista é: {resultado}")