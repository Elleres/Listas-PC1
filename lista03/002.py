p100 = 0
p101 = 0
p102 = 0
p103 = 0 
p104 = 0
p105 = 0

while True:
    x = int(input("Digite o codigo do que voce deseja pedir: "))
    if x == 100:
        p100 += 1
    elif x == 101:
        p101 += 1
    elif x == 102:
        p102 += 1
    elif x == 103:
        p103 += 1
    elif x == 104:
        p104 += 1
    elif x == 105:
        p105 += 1
    y = input("Deseja mais algo? [S/N]: ")
    if y in 'Nn':
        break
print(f'''{p100} x Cachorro quente: {p100 * 1.2}
{p101} x Bauru simples: {p101 * 1.3}
{p102} x Bauru com ovo: {p102 * 1.5}
{p103} x Hamburguer: {p103 * 1.2}
{p104} x Cheeseburguer: {p104 * 1.3}
{p105} x Refri: {p105}''')