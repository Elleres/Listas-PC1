dic = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}
print("""1: JOSE
2:JOSIAS
3:JORGE
4:JAMAL
5:NULO
6:BRANCO""")
while True:
    dic[int(input('Digite em quem vai seu voto: '))] += 1
    x = input("Deseja continuar? [S/N]")
    if x in 'nN':
        break
print(f'Jose: {dic[1]}\nJosias: {dic[2]}\nJorge: {dic[3]}\nJamal: {dic[4]}\nNulo: {dic[5]}\nBranco: {dic[6]}')
total = dic[1] + dic[2] + dic[3] + dic[4] + dic[5] + dic[6]
print(f'Porcentagem nulos: {(dic[5]/total) * 100}\nBrancos:{(dic[6]/total) * 100}')