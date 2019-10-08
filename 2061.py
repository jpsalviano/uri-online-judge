abas, acoes = [int(i) for i in input().split()]
for a in range(acoes):
    if input() == 'fechou':
        abas += 1
    else:
        abas -= 1

print(abas)
