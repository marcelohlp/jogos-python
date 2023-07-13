import random

import menu_principal
import funcoes_global


def jogar():

    funcoes_global.vazio()

    funcoes_global.apresentacao('Jogo de adivinhação!')

    funcoes_global.vazio()

    dificuldade = funcoes_global.menu_dificuldade()

    funcoes_global.vazio()

    # Variáveis valor máximo
    maximo_facil = 100
    maximo_medio = 1000
    maximo_dificil = 10000

    valor_maximo = funcoes_global.dificuldade_escolhida(dificuldade, maximo_facil, maximo_medio, maximo_dificil)

    numero_aleatorio = random.randrange(1, valor_maximo + 1)

    tentativas = 10
    mostrar_tentativas(tentativas)

    funcoes_global.vazio()

    for rodada in range(1, (tentativas + 1)):

        print('Você está na rodada {} de {}!'.format(rodada, tentativas))

        chute = tratar_entrada(valor_maximo)

        if chute == numero_aleatorio:
            resultado_positivo()
            break
        elif chute > numero_aleatorio:
            print('Você chutou um número maior do que o número secreto!')
        else:
            print('Você chutou um número menor do que o número secreto!')

        funcoes_global.vazio()

        if (chute != numero_aleatorio) and (rodada == tentativas):
            resultado_negativo(numero_aleatorio)

    funcoes_global.vazio()

    entrada = funcoes_global.entrada_menu('Jogar novamente', 'Menu principal', 'Finalizar a aplicação')
    funcoes_global.menu_selecao(entrada, jogar, menu_principal.menu_inicial, funcoes_global.finalizar)


def mostrar_tentativas(tentativas):
    print('Você tem {} tentativas'.format(tentativas))


def tratar_entrada(ate_numero):
    while True:
        try:
            chute = int(input('Chute um número entre 1 e {}: '.format(ate_numero)))
            while (chute <= 0) or (chute > ate_numero):
                print("Chute inválido!")
                chute = int(input('Chute um número entre 1 e {}: '.format(ate_numero)))
            return chute
        except ValueError:
            print("Você deve chutar um número inteiro!")
            continue


def resultado_positivo():
    print('Parabéns! Você acertou!')


def resultado_negativo(numero):
    print('Infelizmente você errou... O número era {}.'.format(numero))


if __name__ == '__main__':
    jogar()
