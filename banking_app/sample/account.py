"""
Account class file

Author: Edward Haigh
Created: September 2016
"""


class Account:

    # Private variables

    __name = ""
    __account_number = 0
    __balance = 0.00
    __amount_transferred = 0

    # Set up class

    def __init__(self, name, account_number, balance=0):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def __str__(self):
        return "Name: {}, Account Number: {}, Balance: {}".format(self.__name, self.__account_number, self.__balance)

    # Getters

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_amount_transferred(self):
        return self.__amount_transferred

    # Class Methods

    def deposit_money(self, amount):
        self.__balance += amount
        return self.__balance

    def transfer_money(self, amount):
        self.__balance -= amount
        self.__amount_transferred += amount
        return self.__balance


class CheckingAccount(Account):
    pass


class SavingsAccount(Account):

    __interest = 1.03

    def __init__(self, name, account_number, balance=0):
        Account.__init__(self, name, account_number, balance)

    def calculate_interest_over_x_years(self, years):
        return (years * self.__interest) * self.get_balance()


class BusinessAccount(SavingsAccount):

    __business_name = ""
    __air_miles = 0

    def __init__(self, name, business_name, account_number, balance=1000):
        Account.__init__(self, name, account_number, balance)
        self.__business_name = business_name

    def calculate_air_miles(self):
        self.__air_miles = self.get_amount_transferred() * 0.01
        return self.__air_miles

    def get_air_miles(self):
        return self.__air_miles


if __name__ == '__main__':
    pass
