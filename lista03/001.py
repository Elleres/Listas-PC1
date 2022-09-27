f1 = 0
f2 = 0
f3 = 0 
f4 = 0


while True:
    x = int(input("Digite um número: "))
    if x < 0:
        break
    if x <= 25:
        f1 += 1
    elif 25 < x <=50:
        f2 += 1
    elif 50 < x <= 75:
        f3 += 1
    elif 75 < x <= 100:
        f4 += 1
print(f"""[0 - 25]: {f1}
[26-50]: {f2}
[51-75]: {f3}
[76-100]: {f4}""")