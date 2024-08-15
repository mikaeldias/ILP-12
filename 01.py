# Escreva um programa para ler e armazenar valores em uma matriz de
# tamanho m por n. A quantidade de linhas e colunas deve ser definida
# pelo usuário e a matriz deve ser inicializada com valor 0 em todas as
# posições. O programa deverá solicitar ao usuário um valor inteiro
# positivo para armazenar em cada uma das posições da matriz. Caso o
# usuário digite um valor negativo, esse valor deverá ser dobrado e
# tornado positivo e em seguida inserido na respectiva posição. Ao final,
# exiba os valores da matriz resultante. Considere que os valores de m=2
# e n=3 e as entradas conforme exemplo:

qtd_linhas = int(input('Digite a quantidade de linhas: '))
qtd_colunas = int(input('Digite a quantidade de colunas: '))

matriz = [[0 for i in range(qtd_colunas)] for j in range(qtd_linhas)] # iniciando a matriz c zeros

for i in range(qtd_linhas):
    for j in range(qtd_colunas):
        valor = int(input(f'Digite um valor para a coluna {i} na linha {j}: '))
        if valor < 0:
            valor = -2 * valor
        matriz [i][j] = valor

for linha in matriz:
    print(linha)


