# receber as palavras
entrada = str(input('Digite palavras separadas por espaço: '))
entrada_lista = entrada.split(' ')
lista_tratada = []
# remover os pontos e virgulas
for palavra in entrada_lista:
    if '.' in palavra or ',' in palavra:
        lista_tratada += [palavra[:-1]]# remove o ulto item da lista
    else:
        lista_tratada += [palavra]

# criando uma lista sem palavras duplicados:
frase_sem_duplicadas = []

for palavra in lista_tratada:
    if palavra not in frase_sem_duplicadas:
        frase_sem_duplicadas += [palavra]

#verificar a quantidade de vezes que uma frase aparece no texto
'''
lista_quantidade = '''