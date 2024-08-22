conjunto_1 = {1, 2, 3, 4}
conjunto_2 = {3, 4, 5, 6}
novo_conjunto = set() # Cria um conjunto vazio e remove possiveis duplicadas

for i in conjunto_1:
    if i in conjunto_2:
        novo_conjunto.add(i)

print(novo_conjunto)