soma = 0
for i in range(0, 4):
    x = int(input(f"Digite a {i + 1} nota: "))
    soma += x
print(f"A média das 4 notas é de: {soma / 4}")
