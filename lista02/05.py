lados = list()
for i in range(3):
    lados.append(float(input("Digite o valor de um dos lados: ")))
lados.sort()
if lados[0] + lados[1] > lados[2]:
    print("É um triângulo", end=' ')
else:
    print("Não é um triângulo :(")
    quit()
if lados[0] == lados[1] == lados[2]:
    print("equilátero :))")
elif lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]:
    print("isósceles :))")
else:
    print("escaleno :))")
