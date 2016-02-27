# Aula de Reposição Python
# Lista de Exercício 2
# Questão 4
# Author GugaInfo

# Leia o nome do cliente e atribua a variável

N = input("Digite o Nome do Cliente Sem Espaços: ")

# Leia o preço do produto e atribua a variável

P = input("Digite o Preço do Produto: ")


# Leia a Quantidade do produto e atribua a variável

Q = input("Digite a quantidade do produto: ")

# Calcule o valor e  atribua a variável
# float() ou double() transforma pra n° real ao invés de %d se usa %f para exibi-los

T = float(P) * float(Q)

# Exibir o Resultado como modelo: Senhor <nome_cliente> seus produtos totalizam R$ X,XX reais.
# para exibir string %s


print("Senhor(A) %s, seus produtos totalizaram R$: %.2f reais." % (N, T))
