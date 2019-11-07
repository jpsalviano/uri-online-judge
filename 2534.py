import sys

entrada = sys.stdin.readlines()
linhas = len(entrada)
linha = 0

while linha < linhas:
    h, q = [int(x) for x in entrada[linha].split()]
    notas = []
    for i in range(linha+1, linha+h+1):
        notas.append(int(entrada[i]))
    notas.sort()
    for i in range(linha+h+1, linha+h+1+q):
        print(notas[-int(entrada[i])])
    linha += h+1+q
