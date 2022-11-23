import numpy as np


c = np.eye(10)
linha = 0
coluna = 0
for i in c:
    for ele in i:
        if ele != 0:
            print(f" c: {coluna} l: Linha {linha}", ele)
        coluna += 1
    coluna = 0
    linha += 1
