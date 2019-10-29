from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    conjuntos = deque()
    for j in range(n):
        quantidade, *elementos = deque(int(i) for i in input().split())
        conjuntos.append(elementos)
    q = int(input())
    for _ in range(q):
        o, x, y = deque(int(i) for i in input().split())
        if (o == 1):
            print(len(list(set(conjuntos[x-1]) & set(conjuntos[y-1]))))
        else:
            print(len(set(conjuntos[x-1] + conjuntos[y-1])))
