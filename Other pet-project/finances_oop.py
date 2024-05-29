# System of managment personal finaces

class CashAccount:
    def __init__(self, money):
        self.__money = money
        print(f'__init__ Money: {self.__money}')

    def get_balance(self):
        print(f'get_balancce: {self.__money}')
        return self.__money

    # Внести сумму в банк
    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
            print(f'Deposit:  {amount}, Money_now:  {self.__money}')
        else:
            print(f'To deposit amount should be > 0. Your amount: {amount}')

    # Вывести сумму из банка
    def withdraw(self, amount):
        if self.__money > 0 and 0 < amount <= self.__money:
            self.__money -= amount
            print(f'Withdraw:  {amount}, Money_now:  {self.__money}')

        elif amount > self.__money:
            print(f'To withdraw amount should be < money_now. Your amount: {amount}, money_now: {self.__money}')

        elif self.__money <= 0:
            print(f'To withdraw monew_now should be > 0. Your money_now:  {self.__money}')

        elif amount <= 0:
            print(f'To withdraw money, amount should be > 0. Your amount: {amount}')


class Transaction:
    def __init__(self, account_cash):
        self.account_cash = account_cash

    def add_transaction(self, amount):
        self.account_cash.deposit(amount)

    def reduce_transaction(self, amount):
        self.account_cash.withdraw(amount)


# for test
'''
person = CashAccount(100)
person.get_balance()
person.deposit(100)

person2 = CashAccount(200)
transaction2 = Transaction(person2)
transaction2.add_transaction(-200)

person2.get_balance()

person2.__money = 1  # не сработает, тк private
person2.get_balance()  # убедимся в этом
'''

'''
person3 = CashAccount(100)
transaction3 = Transaction(person3)
# transaction3.reduce_transaction(1)
transaction3.add_transaction(-1)
person3.get_balance()
'''
