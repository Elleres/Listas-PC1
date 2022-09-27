mouses = {}
while True:
    x = input("Digite o numero de identificação: ")
    falha = int(input("Digite o tipo de falha [1/2/3/4]: "))
    if falha == 0:
        break
    mouses[x] = falha
falhaslista = list(mouses.values())
total = len(falhaslista)
causa = ['precisa de limpeza', 'necessita de esfera',
         'troca cabo ou conector', 'quebrado']
print(f"Total: {total}")
for i in range(4):
    print(
        f'{i+1} - {causa[i]} - {falhaslista.count(i+1)} - {(falhaslista.count(i+1)/total) * 100:.2f}')
