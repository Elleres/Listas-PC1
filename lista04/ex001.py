def incluirNovoNome(nome, *args):
    lista_n = list()
    for i in args:
        lista_n.append(i)
    agenda[nome] = lista_n
    return 0


def incluirTelefone(nome, num):
    if nome in agenda:
        agenda[nome].append(num)
    else:
        qst = input('Essa pessoa não está na lista, deseja adiciona-la?[S/N]')
        if qst in 'nN':
            return print('Ok, sua agenda não foi modificada!')
        else:
            incluirNovoNome(nome, num)
    return 0


def excluirTelefone(nome, num):
    if len(agenda[nome]) == 1:
        agenda.pop(nome)
    else:
        agenda[nome].remove(num)
    return 0


def excluirNome(nome):
    agenda.pop(nome)
    return 0


def consultarTelefone(nome):
    return print(agenda[nome])


agenda = {}
incluirNovoNome("Arthur", 123, 123, 123)
consultarTelefone("Arthur")
print(agenda)
