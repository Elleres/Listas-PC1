from email.headerregistry import AddressHeader


horas = int(input("Quantas horas de traballho mensal?"))
mny_hora = float(input("Quanto você recebe por hora?"))
salario = horas * mny_hora
if salario <= 900:
    ir = 0
elif 900 < salario and salario <= 1500:
    ir = 5
elif 1500 < salario and salario <= 2500:
    ir = 10
elif salario > 2500:
    ir = 20
ir_bruto = salario * (ir/100)
print(f"""Salário bruto: ({horas} * {mny_hora})  : R$ {salario}
(-) IR ({ir}%)                 :R$ {ir_bruto}
(-) INSS (10%)              :R$ {salario * 0.1}
FGTS (11%)                  :R$ {salario * 0.11}
Total de descontos          :R$ {ir_bruto + (salario * 0.1)}
Salário Líquido             :R$ {salario - ir_bruto - (salario * 0.1)}""")
