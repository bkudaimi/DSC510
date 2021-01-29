import locale
'''
This program is a simple cash register program
DSC 510
Week 10 Programming Assignment 10.1
Author: Bilal Kudaimi
August 7, 2020
'''
print('This program is a simple cash register program', '\nDSC 510')
print('Week 10 Programming Assignment 10.1', '\nAuthor: Bilal Kudaimi')
print('August 7, 2020', '\n ')
print('Welcome, User!')

class CashRegister():
    def __init__(self):
        self.totalPrice = 0
        self.itemCount = 0

    def addItem(self, price):
        self.totalPrice += price
        self.itemCount += 1

    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    def getTotal(self):
        return 'The total cost of items in your cart is {}'.format(str(locale.currency(self.totalPrice, grouping=True)))

    def getCount(self):
        return 'The number of items in your cart is {}'.format(str(self.itemCount))


def main():
    C = CashRegister()
    print('Welcome to the fruit store!')
    while True:
        A = input(' '
                  '\n What fruit would you like to buy?' 
                  '\n Press 1 for Apple ($1)'
                  '\n Press 2 for Orange ($1.50)'
                  '\n Press 3 for Pineapple ($2) ')
        if A == '1':
            C.addItem(1)
            print(C.getTotal())
            print(C.getCount())
        elif A == '2':
            C.addItem(1.50)
            print(C.getTotal())
            print(C.getCount())
        elif A == '3':
            C.addItem(2)
            print(C.getTotal())
            print(C.getCount())
        else:
            print("I'm sorry, I didn't quite catch what fruit you wanted")

        cont = input('Would you like to add another fruit or check out?'
                  '\n Press 1 to add another fruit'
                  '\n Press 2 to check out ')
        if cont == '1':
            continue
        elif cont == '2':
            print('Thank you for your fruit purchase. You purchased {} fruit costing {} total'.format(C.itemCount, locale.currency(C.totalPrice, grouping=True)))
            input('Press enter to exit.')
            break

if __name__ == "__main__":
    main()