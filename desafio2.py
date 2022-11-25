from math import sqrt


def temArvore(x1, x2, floresta):  # função para checar se há arvore entre duas arvores
    if abs(x2 - x1) == 1:  # Se x1 = 2 e x2 = 3 a subtração deles vai ser igual a 1 e portanto não há inteiros entre eles, sendo assim, não há arvores
        return False
    else:
        # Iterando pelos elementos entre x1 e x2, a razão do -1 é porque queremos quantos elementos temos ENTRE eles
        for i in range(abs(x1 - x2) - 1):
            # Se houver um elemento em X + 1, portanto há arvores entre eles
            if x1 + (i + 1) in floresta:
                return True
    return False  # Se não houver arvores entre eles, irá retornar falso apos sair do laço


# Função para calcular a distancia entre o topo de duas arvores.
def distTopoArvore(x1, x2, floresta):
    # se essas duas arvores nao estiverem na floresta, retorna falso
    if x1 not in floresta or x2 not in floresta:
        return False
    y1 = floresta[x1]  # Caso contrario vai calcular a distancia
    y2 = floresta[x2]
    c1 = abs(y2 - y1)
    c2 = abs(x2 - x1)
    # Pitagoras porem aplicado a plano cartesiano
    d = round(sqrt((c1 ** 2) + (c2 ** 2)), 2)
    return d


    # Algoritmo pra fazer a floresta com dicionario
n = int(input("Digite a quantidade de arvores na floresta: "))
floresta = dict()
# Obi = macaco fofo

for i in range(n):  # Laço pra receber posição e altura de cada arvore
    x = int(input(f"Digite a posição da {i + 1} arvore: "))
    while x in floresta:
        x = int(
            input("Digite um valor válido, não podem haver duas arvores na mesma posiçao: "))
    y = int(input(f"Digite a altura da {i + 1} arvore: "))
    # Inserindo em um dicionario porque não pode haver 2 arvores em um mesmo lugar
    floresta[x] = y
# Organizando pelo x para fazer a floresta, na questão ele passa uma entrada em que não está na ordem
floresta_organizada = dict(sorted(floresta.items()))

print(temArvore(3, 5, floresta_organizada))
# Como calcular para qual arvore Obi deve pular
