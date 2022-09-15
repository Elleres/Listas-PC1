lista_velt = list()
rl = list()
n_tracajah = int(input("Quantos tracajás tem no grupo: "))
for i in range(n_tracajah):
    lista_velt.append(
        float(input(f"Digite a velocidade do tracajá {i + 1}: ")))
for i, x in enumerate(lista_velt):
    if x > 25 or x < 0:
        print(f"Há um erro na velocidade do tracajá {i + 1}")
        rl.append(x)
lista_vel2 = list(lista_velt)
for i in rl:
    lista_velt.remove(i)
max = int(max(lista_velt))
mais_rapido = lista_vel2.index(max) + 1
print(f"O cavalo mais rápido é o: {mais_rapido}")
if max < 10:
    print("Nível 1")
elif 10 <= max < 15:
    print("Nível 2")
elif max >= 15:
    print("Nível 3")
