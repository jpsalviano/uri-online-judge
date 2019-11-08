while True:
    try:
        n, amin, amax = [int(x) for x in input().split()]
        count = 0
        for i in range(n):
            altura = int(input())
            if (amin <= altura <= amax):
                count += 1
        print(count)
    except EOFError:
        break
