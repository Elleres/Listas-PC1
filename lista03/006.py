notas = list()
nome = input("Digite o nome do atleta: ")
for i in range(7):
    notas.append(float(input(f"Nota do jurado {i + 1}:")))
notas2 = list(notas)
pior = min(notas)
mior = max(notas)
notas.remove(pior)
notas.remove(mior)
media = sum(notas)/len(notas)
print(f"Atleta: {nome} ")
for i in notas2:
    print(f'Nota: {i}')
print(f"""Resultado final: 
Atleta: {nome}
Melhor nota: {mior}
Pior nota: {pior}
Media: {media}""")
