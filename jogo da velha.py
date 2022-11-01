import os
from random import randint
from time import sleep


class Player1:
    nome = ''
    vitorias = 0
    preench_j_1 = []
    dific = 0

    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0


class Player2:
    nome = ''
    vitorias = 0
    preench_j_2 = []
    dific = 0

    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0


def num_concat(x, y):
    z = str(x) + str(y)
    return int(z)


def menus(*texto):
    """
    Padroniza os separadores, menus e listas de opções.
    :param texto: não coloque nada para apenas uma linha divisória, coloque
    apenas um item para obter um letreiro mais chamativo, adicione mais de um item para
    lista de opções numeradas.
    :return: retorna o texto, ou textos, inseridos já formatados ou uma linha divisória
    caso parâmetro vazio.
    """
    cores = {'cor1': '\033[7:32:40m', 'cor2': '\033[31m', 'cor3': '\033[33m', 'cor4': '\033[34m', 'limpar': '\033[m'}
    if len(texto) == 0:
        print('=' * 30)
    elif len(texto) == 1:
        print(f'{cores["cor2"]}~~{cores["limpar"]}' * (len(texto[0])))
        print(f'{cores["cor1"]}{texto[0]:^27}{cores["limpar"]}'.center((len(texto) + 3)))
        print(f'{cores["cor2"]}~~{cores["limpar"]}' * (len(texto[0])))
    else:
        for a in range(0, len(texto)):
            print(f'\033[7:36m[{a+1:^3}]\033[m - \033[1:34m', texto[a], ' \033[m')


def pede_num_int(texto, textoc='Erro', limite=0, zero=True):
    """
    Aceita a entrada de números inteiros apenas.
    :param texto: escreva o texto/pedido para o usuário.
    :param textoc: texto de número inválido. (Padrão: 'Erro')
    :param limite: limite permitido para a entrada; se maior, será
    :param zero: Ativa ou desativa a aceitação do número 0. (Padrão: 'Aceita')
    pedido novamente, um valor válido.
    :return: retorna o valor digitado pelo usuário.
    """
    lock1 = True
    while lock1 is True:
        try:
            while True:
                num = int(input(texto))
                if num > limite:
                    print(textoc)
                else:
                    if zero is False:
                        if num == 0:
                            print(textoc)
                        else:
                            break
        except (ValueError, TypeError):
            print(textoc)
        else:
            lock1 = False
            return num


def pede_s_ou_n(texto):
    lock1 = True
    while lock1 is True:
        simounao = str(input(texto)).strip()
        if simounao in 'SsNn' and len(simounao) == 1:
            lock1 = False
            return simounao
        else:
            print('Por favor, digite apenas  ''S'' ou ''N''.')


def pede_palavras(texto, ma=1):
    lock1 = True
    while lock1 is True:
        nome = str(input(texto)).strip()
        if (nome.replace(' ', '')).isalpha() is True:
            if len(nome) < ma:
                lock1 = False
                return nome
            else:
                print(f'A palavra deve ter menos de {ma} caracteres.')
        else:
            print('Por favor, digite apenas letras.')


def pede_nomes():
    Player1.nome = pede_palavras('Digite o nome do jogador nº 1: ', 10)
    Player2.nome = pede_palavras('Digite o nome do jogador nº 2: ', 10)


def modos_de_jogo():
    menus('MODOS DE JOGO')
    menus('Jogar Vs Jogador', 'Jogador Vs PC', 'PC Vs PC')
    print()
    escolha = pede_num_int('Iniciar modo: ', 'Entrada inválida', 3, False)
    return escolha


def tempo(texto, tmp, vz):
    count = 0
    while True:
        print(texto)
        print('.')
        sleep(tmp)
        limpar_tela()
        print(texto)
        sleep(tmp)
        print('..')
        sleep(tmp)
        limpar_tela()
        print(texto)
        sleep(tmp)
        print('...')
        sleep(tmp)
        limpar_tela()
        print(texto)
        sleep(tmp)
        limpar_tela()
        count += 1
        if count == vz:
            break


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_jogo(titulo=True):
    cores = {'cor1': '\033[31m', 'limpa': '\033[m'}
    if titulo is True:
        menus('JOGO DA VELHA')
    print()
    print(f'     {"V":^6}     {"V":^6}     {"V":^6}')
    print(f'     {1:^6}     {2:^6}     {3:^6}')
    print(f'           | |        | |')
    print(f' H1 {cores["cor1"]}{str(mesa[0]):^6}{cores["limpa"]} | | {cores["cor1"]}{str(mesa[1]):^6}{cores["limpa"]}'
          f' | | {cores["cor1"]}{str(mesa[2]):^6}{cores["limpa"]}')
    print(f'           | |        | |')
    print('    ----------------------------')
    print('    ----------------------------')
    print(f'           | |        | |')
    print(f' H2 {cores["cor1"]}{str(mesa[3]):^6}{cores["limpa"]} | | {cores["cor1"]}{str(mesa[4]):^6}{cores["limpa"]}'
          f' | | {cores["cor1"]}{str(mesa[5]):^6}{cores["limpa"]}')
    print(f'           | |        | |')
    print('    ----------------------------')
    print('    ----------------------------')
    print(f'           | |        | |')
    print(f' H3 {cores["cor1"]}{str(mesa[6]):^6}{cores["limpa"]} | | {cores["cor1"]}{str(mesa[7]):^6}{cores["limpa"]}'
          f' | | {cores["cor1"]}{str(mesa[8]):^6}{cores["limpa"]}')
    print(f'           | |        | |')
    print()


def primeiro_jogador():
    if modo == 1 or modo == 2:
        humano_1()
    elif modo == 3:
        ia_1()


def segundo_jogador():
    if modo == 1:
        humano_2()
    elif modo == 2 or modo == 3:
        ia_2()


def ia_1():
    n = 0
    j = 0
    print(f'Jogador número 1 {Player1.nome}: ')
    pare = 0
    dif = randint(1, 10)
    if Player1.dific < dif:
        burro = True
    else:
        burro = False
    lista = [[11, 21, 31], [12, 22, 32], [13, 23, 33], [11, 12, 13],
             [21, 22, 23], [31, 32, 33], [11, 22, 33], [13, 22, 31]]
    opt = [11, 21, 31, 12, 22, 32, 13, 23, 33]

    while pare == 0:

        if 22 not in preenchtt and burro is False:
            n = 22
        if n == 0:
            for u in range(0, len(lista)):
                y = [p for p in lista[u] if p not in Player1.preench_j_1]
                if len(y) == 1:
                    j = y[0]
                    if j not in preenchtt:
                        n = j
            if burro:
                while True:
                    t = opt[randint(0, len(opt) - 1)]
                    if t != j:
                        if t not in preenchtt:
                            n = t
                            break
        if n == 0:
            for u in range(0, len(lista)):
                y = [p for p in lista[u] if p not in Player2.preench_j_2]
                if len(y) == 1:
                    j = y[0]
                    if j not in preenchtt:
                        n = j
            if burro:
                while True:
                    t = opt[randint(0, len(opt) - 1)]
                    if t != j:
                        if t not in preenchtt:
                            n = t
                            break
        if n == 0:
            while True:
                alea = randint(0, 8)
                n = opt[alea]
                if n not in preenchtt:
                    break

        for p in range(0, 9):
            if opt[p] == n:
                sleep(1.5)
                mesa[p] = str(Player1.nome[0:3])
                sleep(0.5)
                preenchtt.append(n)
                Player1.preench_j_1.append(n)
                pare = 12


def ia_2():
    n = 0
    j = 0
    print(f'Jogador número 2 {Player2.nome}: ')
    pare = 0
    dif = randint(1, 10)
    if Player2.dific < dif:
        burro = True
    else:
        burro = False
    lista = [[11, 21, 31], [12, 22, 32], [13, 23, 33], [11, 12, 13],
             [21, 22, 23], [31, 32, 33], [11, 22, 33], [13, 22, 31]]
    opt = [11, 21, 31, 12, 22, 32, 13, 23, 33]

    while pare == 0:

        if 22 not in preenchtt and burro is False:
            n = 22
        if n == 0:
            for u in range(0, len(lista)):
                y = [p for p in lista[u] if p not in Player2.preench_j_2]
                if len(y) == 1:
                    j = y[0]
                    if j not in preenchtt:
                        n = j
            if burro:
                while True:
                    t = opt[randint(0, len(opt) - 1)]
                    if t != j:
                        if t not in preenchtt:
                            n = t
                            break
        if n == 0:
            for u in range(0, len(lista)):
                y = [p for p in lista[u] if p not in Player1.preench_j_1]
                if len(y) == 1:
                    j = y[0]
                    if j not in preenchtt:
                        n = j
            if burro:
                while True:
                    t = opt[randint(0, len(opt) - 1)]
                    if t != j:
                        if t not in preenchtt:
                            n = t
                            break
        if n == 0:
            while True:
                alea = randint(0, 8)
                n = opt[alea]
                if n not in preenchtt:
                    break

        for p in range(0, 9):
            if opt[p] == n:
                sleep(1.5)
                mesa[p] = str(Player2.nome[0:3])
                sleep(0.5)
                preenchtt.append(n)
                Player2.preench_j_2.append(n)
                pare = 1


def humano_1():
    opt = [11, 21, 31, 12, 22, 32, 13, 23, 33]
    print(f'Jogador número 1 {Player1.nome}: ')
    pare = 0
    while pare == 0:
        v = pede_num_int('Vertical: ', 'Retorno inválido', 3, zero=False)
        h = pede_num_int('Horizontal: ', 'Retorno inválido', 3, zero=False)
        n = num_concat(v, h)
        if n in preenchtt:
            limpar_tela()
            mostrar_jogo()
            print("Já marcado")
        else:
            for p in range(0, 9):
                if opt[p] == n:
                    mesa[p] = str(Player1.nome[0:3])
                    preenchtt.append(n)
                    Player1.preench_j_1.append(n)
                    pare = 1


def humano_2():
    opt = [11, 21, 31, 12, 22, 32, 13, 23, 33]
    print(f'Jogador número 2 {Player2.nome}: ')
    pare = 0
    while pare == 0:
        v = pede_num_int('Vertical: ', 'Retorno inválido', 3, zero=False)
        h = pede_num_int('Horizontal: ', 'Retorno inválido', 3, zero=False)
        n = num_concat(v, h)
        if n in preenchtt:
            limpar_tela()
            mostrar_jogo()
            print("Já marcado")
        else:
            for p in range(0, 9):
                if opt[p] == n:
                    mesa[p] = str(Player2.nome[0:3])
                    preenchtt.append(n)
                    Player2.preench_j_2.append(n)
                    pare = 1


def verificar_vitoria(jogadas, nome):
    global brk
    l1 = [11, 12, 13, 11, 21, 31, 11, 31]
    l2 = [21, 22, 23, 12, 22, 32, 22, 22]
    l3 = [31, 32, 33, 13, 23, 33, 33, 13]
    if len(preenchtt) == 9:
        limpar_tela()
        menus('Fim da partida, ninguém ganhou.')
        mostrar_jogo(False)
        brk = 1
    else:
        for o in range(0, 8):
            lista = []
            lista.append(l1[o]), lista.append(l2[o]), lista.append(l3[o])
            count = 0
            for u in range(0, len(jogadas)):
                if jogadas[u] in lista:
                    count += 1
            if count == 3:
                limpar_tela()
                menus(f'Vitoria de {nome} !!!')
                brk = 1
                if jogadas is Player1.preench_j_1:
                    Player1.vitorias += 1
                elif jogadas is Player2.preench_j_2:
                    Player2.vitorias += 1
                mostrar_jogo(False)


def mostrar_placar():
    limpar_tela()
    global brk2
    menus(f'Placar geral: {Player1.nome}: {Player1.vitorias}, {Player2.nome}: {Player2.vitorias}')
    menus()
    fim = pede_s_ou_n('Reiniciar? [S/N]')
    menus()
    if fim in 'Nn':
        brk2 = 1


def pede_dificuldade():
    if modo == 2:
        Player2.dific = pede_num_int(
            f'Digite a dificuldade de {Player2.nome} [1-10]: ', textoc='Entrada inválida', zero=False, limite=10)
    elif modo == 3:
        Player1.dific = pede_num_int(
            f'Digite a dificuldade de {Player1.nome} [1-10]: ', textoc='Entrada inválida', zero=False, limite=10)
        Player2.dific = pede_num_int(
            f'Digite a dificuldade de {Player2.nome} [1-10]: ', textoc='Entrada inválida', zero=False, limite=10)


brk = 0
brk2 = 0
while True:
    if brk2 == 1:
        break
    limpar_tela()
    menus('JOGO DA VELHA')
    modo = modos_de_jogo()
    pede_nomes()
    pede_dificuldade()
    limpar_tela()
    tempo('Sorteando o primeiro a jogar.', 0.1, 2)
    sort = randint(0, 1)
    if sort == 0:
        print(f'O primeiro a jogar será o {Player1.nome}.')
    elif sort == 1:
        print(f'O primeiro a jogar será o {Player2.nome}.')
        sleep(2)
        limpar_tela()
    while True:
        brk = 0
        brk2 = 0
        mesa = [[], [], [], [], [], [], [], [], []]
        preenchtt = []
        Player1.preench_j_1 = []
        Player2.preench_j_2 = []

        while True:
            mostrar_jogo()

            if sort == 0:
                primeiro_jogador()
                verificar_vitoria(Player1.preench_j_1, Player1.nome)
            elif sort == 1:
                segundo_jogador()
                verificar_vitoria(Player2.preench_j_2, Player2.nome)

            if brk == 1:
                break
            limpar_tela()
            mostrar_jogo()

            if sort == 0:
                segundo_jogador()
                verificar_vitoria(Player2.preench_j_2, Player2.nome)
            elif sort == 1:
                primeiro_jogador()
                verificar_vitoria(Player1.preench_j_1, Player1.nome)

            if brk == 1:
                break
            limpar_tela()

        cont = pede_s_ou_n('Continuar jogando:[S/N] ')
        if cont in 'Nn':
            mostrar_placar()
            break
        else:
            if sort == 0:
                sort = 1
            else:
                sort = 0
            limpar_tela()
