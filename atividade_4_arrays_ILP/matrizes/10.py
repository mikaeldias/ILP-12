qtd_linhas = 3
qtd_colunas = 3
impares = []

matriz = [[0 for i in range(qtd_colunas)] for j in range(qtd_linhas)]

for i in range(qtd_linhas):
    for j in range(qtd_colunas):
        entradas = int(input(f'Digite um valor para linha {i} na coluna {j}'))
        if entradas % 2 != 0:
            impares.append(entradas)
        matriz [i][j] = entradas

for linha in matriz:
    print(linha)
print(len(impares))