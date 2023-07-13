import funcoes_global
import forca
import adivinhacao


def menu_inicial():

    funcoes_global.vazio()

    funcoes_global.apresentacao('MENU PRINCIPAL')

    funcoes_global.vazio()

    entrada = funcoes_global.entrada_menu('Jogo forca', 'Jogo adivinhação', 'Finalizar a aplicação')
    funcoes_global.menu_selecao(entrada, forca.jogar, adivinhacao.jogar, funcoes_global.finalizar)


if __name__ == '__main__':
    menu_inicial()
