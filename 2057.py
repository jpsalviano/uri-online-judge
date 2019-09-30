saida, duracao, fuso = [int(i) for i in input().split()]
chegada = saida + duracao + fuso
if chegada < 0:
    chegada += 24
elif chegada > 23:
    chegada -= 24
print('{}'.format(chegada))
