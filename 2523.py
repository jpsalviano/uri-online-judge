import sys

entrada = sys.stdin.readlines()
linhas = len(entrada)
l = 0

while l < linhas:
    cifra = entrada[l].strip()
    trad = ''
    palavra = entrada[l+2].strip().split()
    for n in palavra:
        trad += cifra[int(n)-1]
    print(trad)
    l += 3
