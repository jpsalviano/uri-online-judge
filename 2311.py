n = int(input())

for _ in range(n):
    c = input()
    gd = float(input())
    notas = [float(x) for x in input().split()]
    notas.remove(max(notas))
    notas.remove(min(notas))
    print('{} {:.2f}'.format(c, sum(notas)*gd))
