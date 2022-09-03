qnt_litros = int(input("Digite a quantidade em litros: "))
tipo = input("Digite o tipo de combustível [A/G]:")
valor = qnt_litros * 1.9 if tipo in 'Aa' else qnt_litros * 2.5
if tipo in "Gg":
    d20 = 0.96
    d21 = 0.96
elif tipo in "Aa":
    d20 = 0.97
    d21 = 0.95
if qnt_litros > 20:
    valorf = valor * (d21)
elif qnt_litros <= 20:
    valorf = valor * d21
print(f"O valor a ser pago é de R${valorf}")
