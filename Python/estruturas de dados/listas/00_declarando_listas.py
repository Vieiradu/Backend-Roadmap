'''
    Listas em Python podem armazenar de maneira sequêncial qualquer tipo de objeto. Podemos criar listas:
        -utilizando o construtor *list*
        -a função *range*
        -colocando valores separdos por virgulas dentro de colchetes.

    Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

'''

frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = [] #declara lista vazia
print(frutas)

letras = list("python") #o construtor "list" pede argumento iteravel
print(letras)

numeros = list(range(10)) #aqui cria um elemento para cada função range
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


"""
        ### Acesso Direto ###

    Uma forma de se acessar uma lista é de forma direta:
        -Lista é uma sequência, portanto podemos acessar seus dados utilizando índice.
        -Contamos o índice de determinada sequência a partir do zero.

"""

frutas = ["laranja", "maca", "uva"]
##Sequencias supotam indexação negativa. Ou seja a contagem começa em -1
frutas[-1]
frutas[-3]



'''
        ### Listas Aninhadas ###
    
    Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter
    listas que armazenam outras listas. Com isso podemos criar estruturas:
        -Bidimensionais(tabelas)
        -Acesso informando índices de linha e coluna
    
'''

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) #acessa a primeira linha
print(matriz[0][1]) #acessa a primeira linha e a segunda coluna
print(matriz[-1][-1]) #acessa a ultima linha e a ultima coluna

'''
        ### Fatiamento ###
    
    Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência.
    Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda
    informar quantas posições o cursor deve "pular" no acesso.

'''

       #0123456789  
nome = "Luiz Eduardo David Vieira"

print(nome[0])#pega primeira letra
print(nome[-2])#pega a segunda posição começando do final
print(nome[:9])#começa do 0 e vai até a 9 posição
print(nome[10:])#começa da 10 posição e vai até o fim da string
print(nome[10:16])#começa na 10 e termina na posição 16
print(nome[:])#pega a string completa
print(nome[::-1])#Inverte a ordem da string

'''
        ### Iterar Listas ###

    A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.


'''

frutas = ["laranja", "maca", "uva"]

for fruta in frutas:
    print(fruta)

'''
        ### Função Enumerate ###

    As vezes é necessário saber qual o índice do objeto dentro do laço *for*. 
    Para isso podemos usar:
        -Função *enumerate*

'''

for indice, fruta in enumerate(frutas):
    print(f'{indice}: {fruta}')

'''
        ### Compreensão de Lista (List Compreetion) ###
    
    A compreensão de lista oferece uma sintaxe mais curta quando você deseja:
        -Criar novas listas com base nos valores de uma lista existente(filtro)
        -Gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente
    
'''

## Filtro Versão 1

numeros = [1, 30, 21, 2 , 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# Filtro Versão 2

numeros = [1, 30, 21, 2 , 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

#modificando valores v1

numeros = [1, 30, 21, 2 , 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)