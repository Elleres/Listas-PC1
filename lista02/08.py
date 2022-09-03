date = input("Digite uma data no formato dd/mm/yyyy: ")
datesplit = date.split('/')
ano = int(datesplit[2])
mes = int(datesplit[1])
dia = int(datesplit[0])
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    sn = True
else:
    sn = False
dic = {
    'jan': 31,
    'feb': 28,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31,
}

dicmeses = {
    1: 'jan',
    2: 'feb',
    3: 'mar',
    4: 'apr',
    5: 'may',
    6: 'jun',
    7: 'jul',
    8: 'aug',
    9: 'sep',
    10: 'oct',
    11: 'nov',
    12: 'dec'
}
mestxt = dicmeses[mes]
if sn == True:
    dic['feb'] = 29
if mes > 12 or mes < 1:
    print("Data inválida")
    quit()
if dia > dic[mestxt]:
    print("Data inválida")
    quit()
print("Data válida!")
