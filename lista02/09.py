num = int(input("Digite um número menor que 1000: "))
cent = num // 100
restodez = num % 100
dez = restodez // 10
uni = restodez % 10
if cent == 1:
    print(f"{cent} centena", end='')
elif cent == 0:  # DEIXAR ESPAÇO VAZIO CASO CENTENA SEJA = 0
    True
else:
    print(f"{cent} centenas", end='')
if dez > 0 and uni > 0 and cent > 0:
    print(',', end=' ')
# E CASO TENHA APENAS UNIDADE OU APENAS DEZENAS
elif dez == 0 and uni > 0 and cent > 0 or uni == 0 and dez > 0 and cent > 0:
    print(' e', end=' ')
elif dez == 0 and uni == 0 and cent > 0:  # ESPAÇO VAZIO PRA CASO UNIDADE E DEZENA = 0
    True
if dez == 0:
    True
elif dez == 1:
    print(f"{dez} dezena", end=' ')
else:
    print(f"{dez} dezenas", end=' ')
if uni > 0 and dez > 0:
    print('e', end=' ')
else:
    True
if uni == 0:
    True
elif uni == 1:
    print(f"{uni} unidade")
else:
    print(f"{uni} unidades")
