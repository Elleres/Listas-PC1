def aprovados(d):
    list_aprovados = list(d.keys())
    for aluno in d:
        for nota in d[aluno]:
            if nota < 7:
                list_aprovados.remove(aluno)
                break
    return list_aprovados


d = {'Darth Vader': (7.5, 8.0, 6.5), 'Han   Solo': (
    9.0, 8.5, 9.5), 'Chewbacca': (3.5, 1.0, 6.5)}

print(aprovados(d))
