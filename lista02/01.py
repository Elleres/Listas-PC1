sal_atual = float(input("Insira o salário: "))
dic = {280: 20,
       700: 15,
       1500: 10,
       1000000: 5}
for i, x in dic.items():
    if sal_atual <= i:
        perc = x
        break
aumento = sal_atual*(perc / 100)
print(f'''Salário antes do reajuste: {sal_atual}
Percentual de aumento aplicado: {perc}
Valor do aumento: {aumento}
Valor após aumento: {sal_atual + aumento}''')
