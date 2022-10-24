band = {'verde': 0.50,
        'amarela': 0.53,
        'vermelha': 0.56
        }
equip = {'ar-condicionado': 1600,
         'computador': 350,
         'chuveiro': 5000,
         'ferro': 1000,
         'lampada': 32,
         'lavadora-roupas': 600,
         'refrigerador': 350,
         'tv': 200,
         }
bandeira = input('Digite a bandeira: ')
icms = float(input('Digite o icms: '))
qnt = int(input('Digite a quantidade de equipamentos: '))
equip_tempo = list()
list_temp = list()
for e in range(qnt):
    list_temp.clear()
    list_temp.append(input('Digite o nome do equipamento: '))
    list_temp.append(float(input('Digite o tempo de uso em horas: ')))
    equip_tempo.append(list(list_temp))
s = 0
for i in equip_tempo:
    s += (equip[i[0]] * i[1])
kwh = s/1000
custo_bandeira = kwh * band[bandeira]
custo_final = custo_bandeira * (1 + icms)
print(custo_final)
