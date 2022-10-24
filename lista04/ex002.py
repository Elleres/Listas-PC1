# shift alt a
n_corredores = 0
lista_temp = list()
tempos = dict()
while n_corredores < 6:
    nome_corredor = input('Digite o nome do corredor: ')
    n_voltas = 0
    while n_voltas < 10:
        lista_temp.append(
            int(input(f'Digite o tempo da {n_voltas+1} volta: ')))
        n_voltas += 1
    tempos[nome_corredor] = list(lista_temp)
    lista_temp.clear()
    n_corredores += 1
media_min = dict()
lista = list()
for corredor in tempos:
    media_min[corredor] = [min(tempos[corredor]), sum(
        tempos[corredor])/len(tempos[corredor])]
media_min_items = list(media_min.items())
sort_min_tempo = list(media_min_items)
sort_min_tempo.sort(key=lambda x: x[1][0])
sort_media_tempo = list(media_min_items)
sort_media_tempo.sort(key=lambda x: x[1][1])
print(f"""A melhor volta foi de {sort_min_tempo[0][0]} com tempo de {sort_min_tempo[0][1][0]}
ORDEM DE CHEGADA:""")
for n, corredor in enumerate(sort_media_tempo):
    print(f'{n+1}:{corredor[0]}')
