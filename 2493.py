from sys import stdin

def play_game(expressoes, jogo):
    losers = []
    for i in range(t):
        jogador, indice, operador = jogo[i]
        expressao = expressoes[int(indice)-1].split()
        e1, e2, e3 = int(expressao[0]), int(expressao[1].split('=')[0]), int(expressao[1].split('=')[1])
        if operador == '+':
            if e1 + e2 != e3:
                losers.append(jogador)
        elif operador == '-':
            if e1 - e2 != e3:
                losers.append(jogador)
        elif operador == '*':
            if e1 * e2 != e3:
                losers.append(jogador)
        elif operador == 'I':
            if (e1 + e2 == e3) or (e1 - e2 == e3) or (e1 * e2 == e3):
                losers.append(jogador)
    if len(losers) == t:
        print('None Shall Pass!')
    elif losers == []:
        print('You Shall All Pass!')
    else:
        print(' '.join(sorted(losers)))

entrada = stdin.readlines()
c = 0

while c < len(entrada):
    t = int(entrada[c])
    expressoes = []
    jogo = []
    for i in range(c+1, c+t+1):
        expressoes.append(entrada[i].strip())
        jogo.append([x for x in entrada[i+t].split()])
    play_game(expressoes, jogo)
    c += 1+2*t
