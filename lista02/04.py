nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if 9 <= media <= 10:
    conc = "A"
elif 7.5 <= media < 9:
    conc = "B"
elif 6 <= media < 7.5:
    conc = "C"
elif 4 <= media < 6:
    conc = "D"
elif 0 <= media < 4:
    conc = "E"
print(media, conc, "Aprovado" if conc in "ABC" else "Reprovado")
