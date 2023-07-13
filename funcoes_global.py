

def apresentacao(texto_inicial_str):
    tracejado = ''
    for i in texto_inicial_str:
        tracejado = tracejado + '-'
    print(tracejado)
    print(texto_inicial_str)
    print(tracejado)


def entrada_menu(entrada_um, entrada_dois, finalizar):
    entrada = '0'
    lista_entrada = ('1', '2', '3')
    while entrada not in lista_entrada:
        print('Selecione uma opção!')
        print('(1 - {}) (2 - {}) (3 - {})'.format(entrada_um, entrada_dois, finalizar))
        entrada = input('Digite uma das opções anteriores: ')
    return entrada


def menu_selecao(entrada, opcao_um, opcao_dois, finalizar):
    if entrada == '1':
        opcao_um()
    elif entrada == '2':
        opcao_dois()
    else:
        finalizar()


def menu_dificuldade():
    entrada = '0'
    lista_entrada = ('1', '2', '3')
    while entrada not in lista_entrada:
        print('Menu de seleção de dificuldade')
        print('(1 - fácil) (2 - médio) (3- difícil)')
        entrada = input('Digite uma das opções anteriores: ')
    return entrada


def dificuldade_escolhida(dificuldade, opcao_um, opcao_dois, opcao_tres):
    if dificuldade == '1':
        return opcao_um
    elif dificuldade == '2':
        return opcao_dois
    else:
        return opcao_tres


def finalizar():
    print('Programa finalizado!')
    input('Pressione qualquer tecla para sair!')


def vazio():
    print('')
