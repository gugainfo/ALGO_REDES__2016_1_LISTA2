# Aula de Reposição Python
# Lista de Exercício 2
# Questão 5

# Leia o nome do funcionário

funcionario = input("Digite o nome do funcionário: ")

salario_atual = float(input("Digite o salário atual do mesmo "))


NS = salario_atual + (salario_atual * 0.25)

print("Com o reajuste, o novo salário do funcionário(A): %s será: %.2f" % (funcionario, NS))

