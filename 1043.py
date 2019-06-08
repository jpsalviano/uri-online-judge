# Triangle - 1043

# para ser possível: https://www.youtube.com/watch?v=DBog4PTd-oI
# condições de existência de um triângulo: a) lado x > diferença dos outros dois; b) lado x < soma dos outros dois
# na prática: lado maior tem que ser menor que a soma dos outros dois
# área do trapézio: https://brasilescola.uol.com.br/matematica/quadrilateros-e-trapezio.htm
# area = (B + b)*h/2

A = [float(i) for i in input().split()]
if max(A) < ( sum(A) - max(A) ):
    print('Perimetro = ' + str(sum(A)))
else:
    print('Area = ' + str((A[0]+A[1])*A[2]/2))
