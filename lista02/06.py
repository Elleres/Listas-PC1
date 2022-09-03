from math import sqrt


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C: "))
if a == 0:
    print("A equação não é de segundo grau!")
    quit()
else:
    delta = b**2 - (4*a*c)
    if delta < 0:
        print("A equação não possui raízes reais!")
    elif delta == 0:
        rr = (b * (-1))/(2 * a)
        print(f"A equação possui uma raiz real: {rr}")
    else:
        r1 = ((b * -1) + sqrt(delta)) / (2 * a)
        r2 = ((b * -1) - sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais: {r1} e {r2}")
