# 1018 - Banknotes

'''
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
'''

def banknotesCounter():
    banknotes = [0, 0, 0, 0, 0, 0, 0]
    while True:
        userInput = input('How much would you like to withdraw?\n')
        try:
            totalAmount = int(userInput)
            assert totalAmount >= 0 and totalAmount <= 1000000
            break
        except:
            print('Please type a numeric value, between 0 and 1000000.')
    decomposed = totalAmount
    while decomposed >= 100:
        decomposed -= 100
        banknotes[0] += 1
    while decomposed >= 50:
        decomposed -= 50
        banknotes[1] += 1
    while decomposed >= 20:
        decomposed -= 20
        banknotes[2] += 1
    while decomposed >= 10:
        decomposed -= 10
        banknotes[3] += 1
    while decomposed >= 5:
        decomposed -= 5
        banknotes[4] += 1
    while decomposed >= 2:
        decomposed -= 2
        banknotes[5] += 1
    while decomposed >= 1:
        decomposed -= 1
        banknotes[6] += 1
    print(str(totalAmount) + '\n' + str(banknotes[0]) + ' nota(s) de R$ 100,00'
          + '\n' + str(banknotes[1]) + ' nota(s) de R$ 50,00'
          + '\n' + str(banknotes[2]) + ' nota(s) de R$ 20,00'
          + '\n' + str(banknotes[3]) + ' nota(s) de R$ 10,00'
          + '\n' + str(banknotes[4]) + ' nota(s) de R$ 5,00'
          + '\n' + str(banknotes[5]) + ' nota(s) de R$ 2,00'
          + '\n' + str(banknotes[6]) + ' nota(s) de R$ 1,00')

banknotesCounter()
