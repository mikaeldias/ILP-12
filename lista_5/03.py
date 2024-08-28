# receber os dados

frutas = str(input('Digite nomes de frutas do seu interesse (OBS:separe um item do outro por virgula): '))
verduras = str(input('Digite nome de verduras do seu interesse (OBS:separe um item do outro por virgula): '))

# transformar os dados em uma lista
lista_frutas = frutas.split(', ')
lista_verduras = verduras.split(', ')
# transformar em uma tupla
tupla_frutas = tuple(lista_frutas)
tupla_verduras = tuple(lista_verduras)
# fazer a concatenação das tuplas
tupla_alimentos = lista_frutas + lista_verduras
# apresentar ao usuário

print(tupla_alimentos)