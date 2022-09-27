gabarito = []
ralunos = []
temp = []
for i in range(10):
    gabarito.append(input(f"Digite o gabarito da {i+1} questão: "))

while True:
    for i in range(10):
        temp.append(input(f"Digite a resposta da {i+1} questão:"))
    ralunos.append(list(temp))
    temp.clear()
    x = input("Outro aluno vai usar o programa?[S/N]")
    if x in 'Nn':
        break
notas = []
v = 0
for aluno in ralunos:
    for indx, questao in enumerate(gabarito):
        if gabarito[indx] == aluno[indx]:
            v += 1
    notas.append(int(v))
    v = 0
maior = max(notas)
menor = min(notas)
media = sum(notas)/len(notas)
print(maior, menor, media)
