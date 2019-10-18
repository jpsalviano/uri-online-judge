#2166
def fpc(n):
    f = 0
    for i in range(n):
        f = 1/(2+(f))
    return f

print('{:.10f}'.format(1 + fpc(int(input()))))
