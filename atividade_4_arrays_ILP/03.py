valores = []
qtd_numeros_pares_digitados = 0
while len(valores) < 10:
    entrada = int(input('Digite um numero: '))
    valores.append(entrada)

for i in valores:
    if i % 2 == 0:
        qtd_numeros_pares_digitados += 1
print(f'Quantidade de valores pares: {qtd_numeros_pares_digitados}')