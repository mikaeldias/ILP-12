# resolução questão 6
print('----------Seja Bem Vindo-----------')
lista_numeros = []
lista_string = []

qtd_valores_listas = int(input('\nPor favor, digite a quantidade de itens que deseja adcionar nas listas de numeros e string(Ambas vão conter a mesma quantidade de caracteres): '))
for x in range(qtd_valores_listas):
    numeros = int(input('Digite um número inteiro para adcionar a lista: '))
    string = input('Digite uma letrar para adcionar na lista de strings: ')
    lista_numeros += [numeros]
    lista_string += [string]
    if x % 2 != 0:
        lista_numeros[x] = lista_string[x]

print(lista_numeros)