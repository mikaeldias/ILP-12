# Escreva um programa para ler e armazenar valores em duas matrizes (matriz1
# e matriz2) de tamanho m por n. A quantidade de linhas e colunas deve ser
# definida pelo usuário, bem como os valores de cada matriz. O Programa
# deverá comparar os valores de cada posição e criar uma nova matriz inserindo
# o valor 1, caso o valor matriz1 seja maior que o matriz2, inserir o valor 2 caso
# o valor de matriz2 seja maior que o de matriz1, ou zero caso contrário. Ao final
# exiba os valores das 3 matrizes.

qtd_colunas = int(input('Digite a quantidade de colunas da matriz: '))
qtd_linhas = int(input('Digite a quantidade de linhas da matriz: '))

matriz_1 = [[0 for j in range(qtd_colunas)] for i in range(qtd_linhas)]
matriz_2 = [[0 for j in range(qtd_colunas)] for i in range(qtd_linhas)]
matriz_resultado = [[0 for j in range(qtd_colunas)] for i in range(qtd_linhas)]

# Matriz 1
for j in range(qtd_linhas):
    for i in range(qtd_colunas):
        valor_matriz_1 = int(input(f'Digite um valor para a matriz na coluna {j}, na linha {i}: '))
        matriz_1 [i][j] = valor_matriz_1


# Matriz 2

for j in range(qtd_linhas):
    for i in range(qtd_colunas):
        valor_matriz_2 = int(input(f'Digite um valor para a matriz na linha {i}, na linha {j}: '))
        matriz_2 [i][j] = valor_matriz_2

# matriz resultado maior

for j in range(qtd_linhas):
    for i in range(qtd_colunas):
        if matriz_1 [i][j] > matriz_2 [i][j]:
            matriz_resultado [i][j] = matriz_1 [i][j]
        else:
            matriz_resultado [i][j] = matriz_2 [i][j]



print('-----------------Matriz 1-----------------')
for linha in matriz_1:
    print(linha)

print('-----------------Matriz 2-----------------')
for linha in matriz_2:
    print(linha)

print('-----------------Matriz Resultado-----------------')
for linha in matriz_resultado:
    print(linha)