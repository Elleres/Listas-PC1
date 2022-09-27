while True:
    nome = input("Nome do atleta:")
    if nome == '':
        break
    saltos = list()
    for i in range(5):
        saltos.append(int(input(f"Digite o valor do {i + 1} salto: ")))
    lazy = list(saltos)
    pior = min(saltos)
    mior = max(saltos)
    saltos.remove(pior)
    saltos.remove(mior)
    media = sum(saltos)/len(saltos)
    print(f"""Primeiro salto: {lazy[0]}
    Segundo salto: {lazy[1]}
    Terceiro salto: {lazy[2]}
    Quarto salto: {lazy[3]}
    Quinto salto: {lazy[-1]}
    Melhor salto: {mior}
    Pior salto: {pior}
    Média: {media}
    Resultado
    {nome}:{media}""")
