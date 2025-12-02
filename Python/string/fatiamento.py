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
