menu = {1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50}
valor = 0
for _ in range(int(input())):
    item, quantidade = [int(i) for i in input().split()]
    valor += (menu[item] * quantidade)
print('{:.2f}'.format(valor))
