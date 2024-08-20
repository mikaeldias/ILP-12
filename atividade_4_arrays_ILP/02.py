qtd_valores_lista = int(input('Qual será o tamanho das duas listas?: '))
lista_1 = []
lista_2 = []
soma_pares_lista1 = 0
soma_pares_lista2 = 0
soma_impares_lista1 = 0
soma_impares_lista2 = 0

while len(lista_1) < qtd_valores_lista:
    valores_lista1 = int(input('Digite um valor para ser inserido na lista 1: ')) 
    lista_1.append(valores_lista1)
while len(lista_2) < qtd_valores_lista:
    valores_lista2 = int(input('Digite um valor para ser inserido na lista 2: ')) 
    lista_2.append(valores_lista2)

# calculos lista 1 (par/impar)
for i in lista_1:
    if i % 2 == 0:
        soma_pares_lista1 += 1
    if i % 2 != 0:
        soma_impares_lista1 += 1

# calculos lista 2 (par/impar)
for i in lista_2:
    if i % 2 == 0:
        soma_pares_lista2 += 1
    if i % 2 != 0:
        soma_impares_lista2 += 1

print('Soma dos Pares da lista 1: ',soma_pares_lista1)
print('Soma dos impares da lista 1: ',soma_impares_lista1)
print('Soma dos pares da lista 2: ',soma_pares_lista2)
print('Soma dos impares da lista 2: ',soma_impares_lista2)

# verificando qual somatório da qtd de par é maior
if soma_pares_lista1 > soma_pares_lista2:
    print(f'O somatório dos valores pares da lista 1, é o maior. Totalizando em: {soma_pares_lista1}.') 
else:
    print(f'O somatório dos valores pares da lista 2, é o maior. Totalizando em: {soma_pares_lista2}.') 

# verificando qual somatório da qtd de impar é maior
if soma_impares_lista1 > soma_impares_lista2:
    print(f'O somatório dos valores impares da lista 1, é o maior. Totalizando em: {soma_impares_lista1}.') 
else:
    print(f'O somatório dos valores impares da lista 2, é o maior. Totalizando em: {soma_impares_lista2}.') 

# veficiando se os valores de par são iguais
if soma_pares_lista1 == soma_pares_lista2:
    print('A quantidade de pares da lista 1 é igual a lista de pares da lista 2')

# verficando se os valores impares da listas são iguais
if soma_impares_lista1 == soma_impares_lista2:
    print('A soma dos impares da lista 1 e da lista 2, são iguais.')