contador = 0
lista_entrada = []
qtd_valores_pares = 0
while contador < 10:
    entrada = int(input('Digite um número inteiro: '))
    contador += 1
    lista_entrada.append(entrada)

# verificando se é par
for i in lista_entrada:
    if i % 2 == 0:
        qtd_valores_pares += 1
print(f'Qtd valores par: {qtd_valores_pares}')


