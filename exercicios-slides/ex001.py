# SUBTRAÇAO DE 2 MATRIZES

matriz1 = [[5, 3, 2], [19, 25, 33], [12, 42, 23]]
matriz2 = [[1, 7, 2], [4, 16, 21], [6, 17, 26]]
matrizr = []
mv = []

for i in matriz1:
    matrizr.append(list(mv))  # CRIANDO AS LINHAS DA MATRIZ RESULTANTE

for idx, i in enumerate(matriz1):
    for idx2, ele in enumerate(i):
        matrizr[idx].append(matriz1[idx][idx2] - matriz2[idx][idx2])

print(matrizr)
