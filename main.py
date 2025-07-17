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

# def soma_valores(lista_numeros):
#     resultado = 0
#     for i in lista_numeros:
#         resultado += i
#     return print(resultado)


# soma_valores([87, 24, 56, 12, 99, 3, 74, 45, 61, 30])

# 17 Crie uma função que receba um número como argumento e retorne True se o número 
# for primo e False caso contrário.

# def eh_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return print(False)
#     return print(True)

# eh_primo(4)
# 
# 18 Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# 

# def inverte_palavra(palavra):
#     print(palavra[::-1])

# inverte_palavra("julio")

# 19 Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.


# def soma_combinação(lista,numero):
#     dicionario = {}
#     for each in lista:
#         dicionario[each] = each + numero
#     return print(dicionario)

# soma_combinação([1,2,3],2)

# 
# 20 Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas


def ordena_chaves(dicionario):
    for i in dicionario:
        chave_ordenada = sorted(dicionario.keys())
    return print(chave_ordenada)

ordena_chaves({2030:"julio",2020:"juliana",2010:"ana"})