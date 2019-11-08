while True:
    try:
        n = int(input())
        recorde = 0
        dia = 0
        for _ in range(n):
            dia += 1
            t, d = [int(x) for x in input().split()]
            if d/t > recorde:
                recorde = d/t
                print(dia)
    except EOFError:
        break
