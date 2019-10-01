import sys

# volume = pi * r**2 * h

data = sys.stdin.readlines()
V = [float(i.strip()) for i in data[::2]]
D = [float(i.strip()) for i in data[1::2]]

for i in range(len(V)):
    area = 3.14 * (D[i]/2)**2
    altura = V[i] / area
    print('ALTURA = {:.2f}'.format(altura))
    print('AREA = {:.2f}'.format(area))
