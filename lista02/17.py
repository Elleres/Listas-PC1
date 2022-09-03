fruta = int(input("Qual fruta? [1 maçã / 2 morango]: "))
qntd = int(input("Digite quantos KG: "))
if qntd <= 5:
    morango = 2.5
    maça = 1.8
elif qntd > 5:
    morango = 2.2
    maça = 1.5
valor = qntd * morango if fruta == 2 else qntd * maça
if qntd > 8 or valor > 25:
    valorf = valor * 0.9
print(f"Você deverá pagar R${valorf} pelos {qntd} KG")
