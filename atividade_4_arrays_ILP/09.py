entrada = input('Digite várias palavras separadas por espaço: ')
separando_valores = []

for x in entrada:
    if x != ' ' or x != '.' or x != ',':
        separando_valores.append(x)
print(separando_valores)