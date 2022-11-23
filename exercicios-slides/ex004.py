import numpy as np


tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # CRIA O TABULEIRO


c = 1  # CONTADOR PRA DEFINIR O JOGADOR DA VEZ
while True:
    pos = (int(input("Digite a posicao vertical(0 a 2): ")),  # DEFINIR A POSICAO EM UMA TUPLA (X, Y)
           int(input("Digite a posicao Y(0 a 2): ")))
    if tabela[pos[0]][pos[1]] != 0:  # SE A POSICAO JA ESTIVER OCUPADA POR ALGO Q N SEJA 0
        while tabela[pos[0]][pos[1]] != 0:  # repetir ate inserir posição valida
            pos = (int(input("Digite a posicao vertical valida(0 a 2): ")),
                   int(input("Digite a posicao horizontal valida(0 a 2): ")))
    if c % 2 == 0:  # DEFININDO QUAL JOGADOR MARCAR
        tabela[pos[0]][pos[1]] = 'X'
    else:
        tabela[pos[0]][pos[1]] = 'O'
    c += 1
    print(np.array(tabela))
    # ABAIXO QUEBRA DE VITORIA HORIZONTAL
    if tabela[0][0] == 'X' and tabela[0][1] == 'X' and tabela[0][2] == 'X' or tabela[0][0] == 'O' and tabela[0][1] == 'O' and tabela[0][2] == 'O':
        print('FIM')
        break
    if tabela[1][0] == 'X' and tabela[1][1] == 'X' and tabela[1][2] == 'X' or tabela[1][0] == 'O' and tabela[1][1] == 'O' and tabela[1][2] == 'O':
        print('FIM')
        break
    if tabela[2][0] == 'X' and tabela[2][1] == 'X' and tabela[2][2] == 'X' or tabela[2][0] == 'O' and tabela[2][1] == 'O' and tabela[2][2] == 'O':
        print('FIM')
        break

    # ABAIXO QUEBRA VITORIA VERTICAL
    if tabela[0][0] == 'X' and tabela[1][0] == 'X' and tabela[2][0] == 'X' or tabela[1][0] == 'O' and tabela[2][0] == 'O' and tabela[2][0] == 'O':  # primeira linha vertical
        print('FIM')
        break
    if tabela[0][1] == 'X' and tabela[1][1] == 'X' and tabela[2][1] == 'X' or tabela[0][1] == 'O' and tabela[1][1] == 'O' and tabela[2][1] == 'O':  # segunda linha vertical
        print('FIM')
        break
    if tabela[0][2] == 'X' and tabela[1][2] == 'X' and tabela[2][2] == 'X' or tabela[0][2] == 'O' and tabela[1][2] == 'O' and tabela[0][2] == 'O':  # terceira linha vertical
        print('FIM')
        break

    # ABAIXO QUEBRA DIAGONAL
    if tabela[0][0] == 'X' and tabela[1][1] == 'X' and tabela[2][2] == 'X' or tabela[0][0] == 'O' and tabela[1][1] == 'O' and tabela[2][2] == 'O':  # primeira linha vertical
        print('FIM')
        break
    if tabela[2][0] == 'X' and tabela[1][1] == 'X' and tabela[0][2] == 'X' or tabela[2][0] == 'O' and tabela[1][1] == 'O' and tabela[0][2] == 'O':  # segunda linha vertical
        print('FIM')
        break
    if 0 not in tabela[0] and 0 not in tabela[1] and 0 not in tabela[2]:
        print('empate')
        break
