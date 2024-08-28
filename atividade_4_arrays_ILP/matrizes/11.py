qtd_colunas = int(input('Digite a quantidade de colunas para a matriz: '))
qtd_linhas= int(input('Digite a quantidade de linhas para a matriz: '))

matriz = [[0 for i in range(qtd_colunas)] for j in range(qtd_linhas)]

for i in range(qtd_linhas):
    for j in range(qtd_colunas):
        entrada = int(input(f'Digite um valor para ser armazena na coluna {i} na linha {j}: '))
        matriz[i][j] = entrada
for lista in matriz:
    print(lista)