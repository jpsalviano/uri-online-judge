# Interval - 1037

number = float(input())

if (number < 0) or (number > 100.00):
    print('Fora de intervalo')
elif (number >= 0) and (number <= 25.00):
    print('Intervalo [0,25]')
elif (number > 25.00) and (number <= 50.00):
    print('Intervalo (25,50]')
elif (number > 50.00) and (number <= 75.00):
    print('Intervalo (50,75]')
else:
    print('Intervalo (75,100]')
