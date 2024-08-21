tamanho_lista = int(input('Digite o tamanho da lista: '))
contador_while_1 = 0
contador_while_2 = 0
lista_1 = []
lista_2 = []
lista_intercalada = []

# lista 1
while contador_while_1 < tamanho_lista:
    valores_lista1 = input('Digite um valor para ser armazenado na lista 1: ')
    lista_1.append(valores_lista1)
    contador_while_1 += 1

# lista 2
while contador_while_2 < tamanho_lista:
    valores_lista2 = input('Digite um valor para ser amarenado na lista 2: ')
    lista_2.append(valores_lista2)
    contador_while_2 += 1

# valores intercalados
for i in range(len(lista_1)):
    lista_intercalada.append(lista_1[i])
    lista_intercalada.append(lista_2[i])








print(lista_1)
print(lista_2)
print(lista_intercalada)