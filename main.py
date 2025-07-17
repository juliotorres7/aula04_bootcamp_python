# Exercícios de Listas e Dicionários

# 1 Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista_numeros = []

# for i in range(11):
#     lista_numeros.append(i)

# for j in lista_numeros:
#     print( j**2 )


# 2 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# linguagens = ["Python", "Java", "C++", "JavaScript"]

# linguagens.append("Ruby")

# linguagens.remove("C++")

# print(linguagens)


# 3 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de 
# publicação. Imprima cada informação.

# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}

# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")

# 4 Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

# 5 Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
# calcule o preço total da lista de compras.

# lista_de_compra = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# lista_de_preco = sum(lista_de_compra[item] for item in lista_de_compra)

# print(lista_de_preco)

# Exercícios de Funções
# 16 Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# 

# lista_numeros = [1,2,3,4,5]



def soma_valores(lista_numeros):
    resultado = 0
    for i in lista_numeros:
        resultado += i
    return print(resultado)


soma_valores([87, 24, 56, 12, 99, 3, 74, 45, 61, 30])

# 17 Crie uma função que receba um número como argumento e retorne True se o número 
# for primo e False caso contrário.
# 
# 18 Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# 
# 19 Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 
# 20 Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

