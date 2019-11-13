dodo = 'Os atributos dos monstros vao ser inteligencia, sabedoria...'
leo = "Iron Maiden's gonna get you, no matter how far!"
pepper = 'Urano perdeu algo muito precioso...'
empate = 'Putz vei, o Leo ta demorando muito pra jogar...'
msgs = {'dodo': dodo, 'leo': leo, 'pepper': pepper}

def jogo(j1, j2, j3):
    jogo_dict = {'pedra': 'tesoura', 'papel': 'pedra', 'tesoura': 'papel'}
    vencedores = []
    jogadas = [j1, j2, j3]
    jogadores = ['dodo', 'leo', 'pepper']
    for i, jogada1 in enumerate(jogadas):
        jogadas_restantes = jogadas.copy()
        del jogadas_restantes[i]
        for jogada2 in jogadas_restantes:
            if jogo_dict[jogada1] == jogada2:
                vencedores.append(jogadores[i])
    return list(set(vencedores))

while True:
    try:
        d, l, p = [i for i in input().split()]
        resultado = jogo(d, l, p)
        if len(resultado) == 0 or len(resultado) > 1:
            print(empate)
        else:
            print(msgs[resultado[0]])
    except EOFError:
        break
