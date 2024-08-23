qtd_valores = int(input('Digite a quatidade de valores que serão informados: '))
maior_valor = None
menor_valor = None
soma_valores = 0

for i in range(qtd_valores):
    valores = int(input('Digite um valor para realizar as análises: '))
    if maior_valor is None or valores > maior_valor:
        maior_valor = valores
    if menor_valor is None or valores < menor_valor:
        menor_valor = valores
    soma_valores += valores
    media_aritmética = soma_valores/qtd_valores

print(f'Menor valor: {menor_valor}')
print(f'Maior valor: {maior_valor}')
print(f'Média Aritimética: {media_aritmética}')
    

   