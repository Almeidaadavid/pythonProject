nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
prioridade = "NÃO"
if idade >= 65:
    prioridade = "SIM"
print("O paciente " + nome + " tem prioridade? " + prioridade)
