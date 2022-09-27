salarios = list()
while True:
    s = (int(input("Salario: ")))
    if s == 0:
        break
    salarios.append(s)
abonos = list()
for i in salarios:
    if i * 0.2 < 100:
        abonos.append(100)
    else:
        abonos.append(i * 0.2)
print("Salario:         Abono")
for i, v in enumerate(salarios):
    print(f"""{v}          {abonos[i]} """)
print(f"""Total gasto com abonos: {sum(abonos)}
Colaboradores: {len(salarios)}
Valor minimo: {min(abonos)}
Valor maximo: {max(abonos)}""")
