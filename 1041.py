# Coordinates of a Point - 1041

x, y = [float(i) * 10 for i in input().split()]

# Origem
if ( x == 0 ) and ( y == 0 ):
    print('Origem')

# Eixo X
if ( x != 0 ) and ( y == 0 ):
    print('Eixo X')

# Eixo Y
if ( x == 0 ) and ( y != 0 ):
    print('Eixo Y')

# Q1
if ( x > 0 ) and ( y > 0 ):
    print('Q1')

# Q2
elif ( x < 0 ) and ( y > 0 ):
    print('Q2')

# Q3
elif ( x < 0 ) and ( y < 0 ):
    print('Q3')

# Q4
elif ( x > 0 ) and ( y < 0 ):
    print('Q4')
