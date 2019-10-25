import sys
from math import sqrt

for c in sys.stdin.readlines():
    xf, yf, xi, yi, vi, ru, rc = [int(i) for i in c.split()]
    distance = sqrt((xi - xf)**2+(yi - yf)**2)
    attack_range = ru + rc - (1.5 * vi)
    if distance <= attack_range:
        print('Y')
    else:
        print('N')
