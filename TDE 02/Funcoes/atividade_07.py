# Crie uma função chamada contar_caracteres que receba uma string e um 
# caractere como parâmetros e retorne o número de vezes que o caractere 
# aparece na string.


def contar_caracteres(texto, caractere):
    contador = 0
    for letra in texto:
        if letra == caractere:
            contador += 1
    return contador


texto = "guilherme"
caractere = "e"
resultado = contar_caracteres(texto, caractere)
print(f"O caractere '{caractere}' aparece {resultado} vezes no texto.")

