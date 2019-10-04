import sys

for i, num in enumerate(sys.stdin.readlines(), 1):
    sequencia = [0]
    n = int(num.strip())
    for j in range(n+1):
        for k in range(j):
            sequencia.append(j)
    print('Caso {}: {} numero{}'.format(i, len(sequencia), 's' if n > 0 else ''))
    print(str(sequencia).strip('[]').replace(',', ''))
    print()
