# 1021 - Banknotes and Coins

'''
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
'''

def banknotesAndCoinsCounter():
    banknotes = [0, 0, 0, 0, 0, 0]
    coins = [0, 0, 0, 0, 0, 0]
    totalAmount = float(input()) * 100 # trabalhar com centavos
    decomposed = int(totalAmount)
    while decomposed >= 10000:
        decomposed -= 10000
        banknotes[0] += 1
    while decomposed >= 5000:
        decomposed -= 5000
        banknotes[1] += 1
    while decomposed >= 2000:
        decomposed -= 2000
        banknotes[2] += 1
    while decomposed >= 1000:
        decomposed -= 1000
        banknotes[3] += 1
    while decomposed >= 500:
        decomposed -= 500
        banknotes[4] += 1
    while decomposed >= 200:
        decomposed -= 200
        banknotes[5] += 1
    while decomposed >= 100:
        decomposed -= 100
        coins[0] += 1
    while decomposed >= 50:
        decomposed -= 50
        coins[1] += 1
    while decomposed >= 25:
        decomposed -= 25
        coins[2] += 1
    while decomposed >= 10:
        decomposed -= 10
        coins[3] += 1
    while decomposed >= 5:
        decomposed -= 5
        coins[4] += 1
    while decomposed >= 1:
        decomposed -= 1
        coins[5] += 1
    print('NOTAS:\n' + str(banknotes[0]) + ' nota(s) de R$ 100.00'
          + '\n' + str(banknotes[1]) + ' nota(s) de R$ 50.00'
          + '\n' + str(banknotes[2]) + ' nota(s) de R$ 20.00'
          + '\n' + str(banknotes[3]) + ' nota(s) de R$ 10.00'
          + '\n' + str(banknotes[4]) + ' nota(s) de R$ 5.00'
          + '\n' + str(banknotes[5]) + ' nota(s) de R$ 2.00'
          + '\nMOEDAS:\n' + str(coins[0]) + ' moeda(s) de R$ 1.00'
          + '\n' + str(coins[1]) + ' moeda(s) de R$ 0.50'
          + '\n' + str(coins[2]) + ' moeda(s) de R$ 0.25'
          + '\n' + str(coins[3]) + ' moeda(s) de R$ 0.10'
          + '\n' + str(coins[4]) + ' moeda(s) de R$ 0.05'
          + '\n' + str(coins[5]) + ' moeda(s) de R$ 0.01')


banknotesAndCoinsCounter()
