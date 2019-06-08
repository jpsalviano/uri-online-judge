# Snack - 1038

x, y = [int(i) for i in input().split()]

menu = [400, 450, 500, 200, 150]

totalmsg = 'Total: R$ '

print(totalmsg + str('{:.2f}'.format(menu[x-1] * y * 0.01)))
