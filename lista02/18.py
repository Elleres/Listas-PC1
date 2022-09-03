tipo = int(
    input("1 = Filé\n2 = Alcatra\n3 = Picanha\nDigite qual carne você quer: "))
qnt = float(input("Digite a quantidade de carne a comprar: "))
pag = input("Cartão tabajara? [S/N]")
if qnt <= 5:
    file = 4.9
    alcatra = 5.9
    picanha = 6.9
else:
    file = 5.8
    alcatra = 6.8
    picanha = 7.8
tipodic = {
    1: "Filé",
    2: "Alcatra",
    3: "Picanha"
}
dic2 = {
    1: file,
    2: alcatra,
    3: picanha
}
total = qnt * dic2[tipo]
print(f"""Tipo de carne: {tipodic[tipo]}
Quantidade de carne: {qnt}
Preço total: {total}
Tipo de pagamento: {"tabajara" if pag in "sS" else "outro método"}
Desconto: {total * 0.05 if pag in "sS" else 0}
Valor a pagar: {total*0.95 if pag in "sS" else total}""")
