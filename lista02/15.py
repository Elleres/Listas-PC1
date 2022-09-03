lista = list()
lista.append(input("Telefonou para a vítima? (S/N)"))
lista.append(input("Esteve no local do crime? (S/N)"))
lista.append(input("Mora perto da vítima? (S/N)"))
lista.append(input("Devia para a vítima? (S/N)"))
lista.append(input("Já trabalhou com a vítima? (S/N)"))
c = 0
for i in lista:
    if i in 'Ss':
        c += 1
if c == 2:
    p = "Suspeita"
elif c == 3 or c == 4:
    p = "Cúmplice"
elif c == 5:
    p = "Assassino"
else:
    p = "Inocente"

print(p)
