valor = int(input("Digite o valor: R$"))
notas100 = valor // 100
restante = valor % 100
notas50 = restante // 50
restante = restante % 50
notas10 = restante // 10
restante = restante % 10
notas5 = restante // 5
restante = restante % 5
notas1 = restante // 1
print(f"""Notas de 100: {notas100}
Notas de 50: {notas50}
Notas de 10: {notas10}
Notas de 5: {notas5}
Notas de 1: {notas1}""")
