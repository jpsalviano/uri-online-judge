import sys

entrada = sys.stdin.readlines()
casos = len(entrada)
c = 0

while c < casos:
    m = int(entrada[c])
    notas = []
    cargas = []
    for i in range(c+1, c+1+m):
        nota, carga = [int(x) for x in entrada[i].strip().split()]
        notas.append(nota)
        cargas.append(carga)
    ira = sum([nota*carga for nota, carga in zip(notas, cargas)]) / sum(cargas)
    print('{:.4f}'.format(ira/100))
    c += m + 1
