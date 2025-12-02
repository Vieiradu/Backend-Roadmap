nome = "Eduardo"
idade = 31
profissao = "Programador"
saldo = 21.321

dados = {"nome": "Eduardo", "idade": 31}

print("Nome: %s Idade: %d" %(nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
