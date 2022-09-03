dic = {
    '1': 'Domingo',
    '2': 'Segunda',
    '3': 'Terça',
    '4': 'Quarta',
    '5': 'Quinta',
    '6': 'Sexta',
    '7': 'Sábado'
}
dia = input("Digite um número:")
if dia in dic.keys():
    print(dic[dia])
else:
    print('Número inválido.')
