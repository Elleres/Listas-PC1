peso_peixe = float(input("Digite o peso do peixe: "))
if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(
        f"O peso do peixe é de {peso_peixe} com excesso de {excesso} e é necessário pagar multa de R${multa}")
print(f"O peso do peixe é de {peso_peixe} e não é necessário pagar multa!")
