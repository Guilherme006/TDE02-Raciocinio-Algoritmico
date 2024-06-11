# Crie uma função chamada e_palindromo que receba uma string como 
# parâmetro e retorne True se a string for um palíndromo (ou seja, se lida de trás 
# para frente for igual à original) e False caso contrário.

def e_palindromo(texto):
    
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]


texto = input("Digite uma palavra ou frase: ")


if e_palindromo(texto):
    print(True)
else:
    print(False)


# def e_palindromo():
   
#     texto = input("Digite uma palavra ou frase: ")
    
   
#     texto = texto.replace(" ", "").lower()

#     if texto == texto[::-1]:
#         print(True)
#     else:
#         print(False)
    
    
# e_palindromo()




    
