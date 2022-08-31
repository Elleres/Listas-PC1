from math import ceil


m2 = float(input("Digite quantos metros quadrados deseja pintar: "))
qnt_litros = m2 / 3
qnt_latas = qnt_litros / 18
print(f"Para pintar {m2} m2 será necessário {qnt_litros:.2f} litros o sendo então necessário comprar {ceil(qnt_latas)} latas"
      f" resultando em R${ceil(qnt_latas) * 80}.")
