notas = [1, 36, 61, 86, 101]
conceitos = ['E', 'D', 'C', 'B', 'A']

nota = int(input())

for i, n in enumerate(notas):
    if nota < n:
        print(conceitos[i])
        break
