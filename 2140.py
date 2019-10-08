notas = [2, 5, 10, 20, 50, 100]
trocos_possiveis = list()
for nota1 in notas:
    for nota2 in notas:
        trocos_possiveis.append(nota1 + nota2)
trocos_possiveis = set(trocos_possiveis)

while True:
    n, m = [int(i) for i in input().split()]
    if n == m == 0:
        break
    troco = m - n
    print('{}'.format('possible' if troco in trocos_possiveis else 'impossible'))
