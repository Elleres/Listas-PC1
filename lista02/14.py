n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
t = input("Digite a operação: [x, /, +, -] ")
if t in 'xX':
    r = n1 * n2
elif t == '/':
    r = n1 / n2
elif t == '+':
    r = n1 + n2
elif t == '-':
    r = n1 - n2
else:
    "Operação inválida!"
    quit()
if r % 2 == 0:
    rpi = 'Par'
else:
    rpi = 'Impar'
if r - r == 0:
    rpn = 'Positivo'
else:
    rpn = "Negativo"
if r - (round(r)) != 0:
    rid = "Decimal"
else:
    rid = "Inteiro"
print(f"{r}, é {rpi}, {rpn} e {rid}")
