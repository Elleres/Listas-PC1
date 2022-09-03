ano = int(input("Digite o ano a ser verificado: "))
sn = None
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    sn = True
else:
    sn = False
print(sn)
