inteiros = [] # lista que vai armazenar os valores inputados(apenas inteiros)
valores_impar = []
soma_valores_impar = []

entrada = input('Digite uma sequência de números inteiros, separados por espaço: ') # pegando dados
for x in entrada: # percontendo pelos dados iputados
    if x != ' ': # condição para pegar apenas os numeros
        inteiros.append(int(x)) # colocando na lista interios, os inteiros de i

for y in inteiros:
    if y % 2 != 0:
        valores_impar.append(y)
        
while len(valores_impar) > 1:
    soma_1 = valores_impar[0]
    soma_2 = valores_impar[1]
    soma_total = soma_1 + soma_2
    soma_valores_impar.append(soma_total)
    del valores_impar[0]
print(soma_valores_impar)