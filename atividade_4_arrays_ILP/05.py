qtd_valores = int(input('Digite a quantidade de valores que serão fornecidos: '))
contador = 0
lista_entrada = []
maior_valor = []
menor_valor = []
soma_valores_entrada = 0
while contador < qtd_valores:
    entrada = int(input('Digite um valor para incluir na lista para analise: '))
    lista_entrada.append(entrada)
    contador += 1

for i in lista_entrada:
    if maior_valor == []:
        maior_valor.append(i)
    if i > maior_valor[0]:
        maior_valor = []
        maior_valor.append(i)
    if menor_valor == []:
        menor_valor.append(i)
    if i < menor_valor[0]:
        menor_valor = []
        menor_valor.append(i)

# calculo média aritmetica:
for i in lista_entrada:
    soma_valores_entrada += i
calculo_media_aritmetica = soma_valores_entrada/qtd_valores

print(f'O maior valor é: {maior_valor[0]}')
print(f' O menor valor é: {menor_valor[0]}')
print(f'A média aritmética é igual a: {calculo_media_aritmetica}')

        