lista_vazia = []  # LISTAS VAZIAS PRA TRABALHAR
lista_final = []
lista_nomes = []
lista_max = []  # Cria lista para salvar o tempo maximo de cada corredor
lista_soma = []
dic = {}


for i in range(3):
    # Lista com nomes separada para associar depois aos resultados
    lista_nomes.append(input("Digite o nome do corredor: "))
    for c in range(2):
        # Salva os tempos do corredor em uma lista
        lista_vazia.append(int(input("Digite o tempo dessa volta: ")))
    # Salva na ordem de entrada os resultados dos corredores
    lista_final.append(list(lista_vazia))
    lista_vazia.clear()  # Limpa a lista para repetir o processo


for i in range(len(lista_final[0])):
    dic[i] = 0  # criando a soma de todos os tempos de cada volta
    for c in range(len(lista_final)):
        dic[i] += lista_final[c][i]


for i in dic:
    dic[i] = dic[i] / len(lista_final[0])  # fazendo a media deles

dic_org = sorted(dic.values())

for dados in lista_final:
    # Procura na lista o resultado maximo entre as corridas e salva o index desse resultado para dizer em qual volta ocorreu
    lista_max.append([max(dados), dados.index(max(dados))])


for i in range(len(lista_nomes)):  # Agrupando os nomes e os resultados
    lista_max[i].append(lista_nomes[i])
# Organizando a lista por meio do sorted, organizando pelo primeiro elemento
lista_organizada = sorted(lista_max, key=lambda x: x[0])
print(
    f'A melhor volta foi a do participante {lista_max[0][2]} na volta {lista_max[0][1] + 1} com tempo de {lista_max[0][0]}')
print(f'A menor média foi {dic_org[0]}')

for idx, dados in enumerate(lista_organizada):
    print(f'{idx+1}º: {dados[2]}')
