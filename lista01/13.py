h = float(input("Digite a sua altura: "))
s = input("H: homem; M: mulher.")
if s in "hH":
    print(f"Seu peso ideal é de: {72.7*h - 58}")
elif s in "mM":
    print(f"Seu peso ideal é de: {62.1 * h - 44.7}")
