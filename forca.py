import random
import menu_principal
import funcoes_global


def jogar():

    funcoes_global.vazio()

    funcoes_global.apresentacao('Jogo de forca!')

    funcoes_global.vazio()

    dificuldade = funcoes_global.menu_dificuldade()

    funcoes_global.vazio()

    # Variáveis documento dificuldade
    documento_facil = 'documentos/palavras_faceis.txt'
    documento_medio = 'documentos/palavras_medianas.txt'
    documento_dificil = 'documentos/palavras_dificeis.txt'

    dificuldade_escolhida = funcoes_global.dificuldade_escolhida(dificuldade, documento_facil, documento_medio, documento_dificil)

    palavra_secreta = definido_palavra(dificuldade_escolhida)

    palavra_escondida = escondendo_palavra(palavra_secreta)

    print('Palavra secreta: {}'.format(palavra_escondida))

    funcoes_global.vazio()

    tentativas = 7
    tentativas_restantes(tentativas)

    # Variáveis de controle
    acertou = False
    enforcou = False
    lista_chutes = []

    while (not enforcou) and (not acertou):

        chute, lista_chutes = tratar_chute(lista_chutes)
        print('Letras chutadas: {}'.format(lista_chutes))

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    palavra_escondida[posicao] = letra
                posicao += 1
            if '_' not in palavra_escondida:
                acertou = True
        else:
            tentativas -= 1
            desenha_forca(tentativas)
            tentativas_restantes(tentativas)
            if tentativas == 0:
                enforcou = True
        funcoes_global.vazio()
        print('Palavra secreta: {}'.format(palavra_escondida))
        funcoes_global.vazio()

    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

    funcoes_global.vazio()

    entrada = funcoes_global.entrada_menu('Jogar novamente', 'Menu principal', 'Finalizar a aplicação')
    funcoes_global.menu_selecao(entrada, jogar, menu_principal.menu_inicial, funcoes_global.finalizar)


def definido_palavra(diretorio):
    with open(diretorio, 'r', encoding='UTF-8') as arquivo:
        lista_palavras = []
        for linha in arquivo:
            linha = linha.strip().upper()
            lista_palavras.append(linha)
    numero_aleatorio = random.randrange(len(lista_palavras))
    palavra_secreta = lista_palavras[numero_aleatorio]
    return palavra_secreta


def escondendo_palavra(palavra):
    return ['_' for letra in palavra]


def tentativas_restantes(tentativas):
    print('Você tem {} tentativas!'.format(tentativas))


def tratar_chute(lista_chutes):
    chute = ''
    lista_invalidos = ('ª', 'º', '°')
    while not (chute.isalpha()) or (chute in lista_invalidos) or (len(chute) != 1) or (chute in lista_chutes):
        chute = pede_chute()
        if not (chute.isalpha()) or (chute in lista_invalidos):
            print('Você digitou um caractere inválido! Você precisa digitar uma letra!'.format(chute))
            funcoes_global.vazio()
        elif len(chute) != 1:
            print('Você pode digitar apenas uma letra por vez!')
            funcoes_global.vazio()
        elif chute in lista_chutes:
            print('Você já escolheu esta letra!')
            funcoes_global.vazio()
        else:
            lista_chutes.append(chute)
            funcoes_global.vazio()
            return chute, lista_chutes


def pede_chute():
    return input('Escolha uma letra: ').strip().upper()


def desenha_forca(tentativa):
    print("  _______     ")
    print(" |/      |    ")

    if tentativa == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativa == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if tentativa == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if tentativa == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if tentativa == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativa == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativa == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print('A palavra era {}!'.format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == '__main__':
    jogar()
