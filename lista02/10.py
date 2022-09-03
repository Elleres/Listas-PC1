notas = list()
for i in range(3):
    notas.append(float(input(f"Digite o valor da nota {i + 1}:")))
media = (notas[0] + notas[1] + notas[2]) / 3
if media < 7:
    print("Reprovado")
elif media >= 7 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com distinção")
