sal_hora = float(input("Digite o quanto você recebe por hora: "))
horas = int(input("Digite quantas horas você trabalha por mês: "))
sal_bruto = sal_hora * horas
ir = sal_bruto * 0.11
inss = sal_bruto*0.08
sin = sal_bruto * 0.05
print(f"+ Salário Bruto: R$ {sal_bruto}\n- IR(11%): R${ir}\n"
      f"- INSS(8%): R${inss}\n- Sindicato(5%): R${sin}\n"
      f"=Salário liquido: R${sal_bruto + ir + inss + sin} ")
