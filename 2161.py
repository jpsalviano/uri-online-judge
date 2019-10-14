def fpc(n):
    f = 0
    for i in range(n):
        f = 1/(6+(f))
    return f

print('{:.10f}'.format(3 + fpc(int(input()))))
