# Game Time - 1046

start, end = [int(i) for i in input().split()]
if start == end:
    time = 24
elif start > end:
    time = 24 - start + end
else:
    time = end - start
print('O JOGO DUROU ' + str(time) + ' HORA(S)')
