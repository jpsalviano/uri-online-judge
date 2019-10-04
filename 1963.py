preco_1, preco_2 = [float(i) for i in input().split()]
print('{:.2f}%'.format((preco_2 - preco_1) / preco_1 * 100))
