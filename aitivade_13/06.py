conjunto_palavras = {"arara", "casa", "ovo", "radar"}
palavras_palíndromo = set()
for i in conjunto_palavras:
    invertendo_string = i[::-1]
    if invertendo_string == i:
        palavras_palíndromo.add(invertendo_string)
print(palavras_palíndromo)