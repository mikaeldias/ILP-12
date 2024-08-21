dicionario = {"Brasil": 211.8, "China": 1400.5, "Índia": 1366.4}
maior_pais = 0
pais = ''
for i in dicionario:
    if dicionario[i] > maior_pais:
        maior_pais = dicionario[i]
        pais = i
print(pais, maior_pais)