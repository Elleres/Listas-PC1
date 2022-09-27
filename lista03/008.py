from calendar import c


carros = list()
consumo = list()
for i in range(5):
    carros.append(input("Nome:"))
    consumo.append(int(input("Consumo: ")))
for i in range(0, 4):
    print(
        f'{i + 1} - {carros[i]} - {consumo[i]} - {1000/consumo[i]:.2f} litros -  R${(1000/consumo[i]) * 2.25} ')
posicao = consumo.index(max(consumo))
print(f"O menor consumo é o {carros[posicao]}")
