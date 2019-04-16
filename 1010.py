# 1010 - simple calculate

'''
n this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.
'''

product1 = input()
product2 = input()

product1Data = product1.split()
product2Data = product2.split()

product1Units = int(product1Data[1])
product1Price = float(product1Data[2])

product2Units = int(product2Data[1])
product2Price = float(product2Data[2])

def simpleCalculate(product1Units, product1Price, product2Units, product2Price):
    total1 = product1Units * product1Price
    total2 = product2Units * product2Price
    total = total1 + total2
    print('VALOR A PAGAR: R$ ' + str('{:0.2f}'.format(total)))

simpleCalculate(product1Units, product1Price, product2Units, product2Price)
