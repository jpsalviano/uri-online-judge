# Positive Numbers - 1060

numbers = []

for i in range(6):
    numbers.append(float(input()))

totalPos = 0

for number in numbers:
    if number > 0:
        totalPos += 1

print('{} valores positivos'.format(totalPos))
