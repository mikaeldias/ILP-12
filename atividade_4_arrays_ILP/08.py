entrada = input('Digite valores inteiros, separados por espaço: ')
#list comprehension
lista_string_inteiros = [int(num) for num in entrada.split()] 
so_impar = []
texte = []
for i in lista_string_inteiros:
    if i % 2 != 0:
        so_impar.append(i)
    else:
        pass


while len(so_impar):
    ...