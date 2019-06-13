# Triangle Types - 1045

ABC = [float(i) for i in input().split()]
ABC.sort(reverse=True)
A, B, C = ABC

for i in range(1):
    if A >= (B + C):
        print('NAO FORMA TRIANGULO')
        break
        
    if A**2 == (B**2 + C**2):
        print('TRIANGULO RETANGULO')
        
    if A**2 > (B**2 + C**2):
        print('TRIANGULO OBTUSANGULO')
        
    if A**2 < (B**2 + C**2):
        print('TRIANGULO ACUTANGULO')
        
    if A == B == C:
        print('TRIANGULO EQUILATERO')
        
    if (A == B != C) or (B == C != A) or (C == A != B):
        print('TRIANGULO ISOSCELES')
