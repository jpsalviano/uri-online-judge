#2164
from math import sqrt

def fibonacci(n):
    f = round((((1 + sqrt(5))/2)**n - ((1 - sqrt(5))/2)**5) / sqrt(5))
    print('{:.1f}'.format(f))

fibonacci(int(input()))
