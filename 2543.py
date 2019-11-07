while True:
    try:
        n, i = [int(x) for x in input().split()]
        gameplays = [[int(x) for x in input().split()] for i in range(n)]
        count = 0
        for g in gameplays:
            if (g[0] == i) and (g[1] == 0):
                count += 1
        print(count)
    except EOFError:
        break
