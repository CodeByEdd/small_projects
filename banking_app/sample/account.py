"""
Account class file

This file contains the parent class Account
This file contains the child classes Checking Account, Saving Account, and Business Account

I created this file to practice Class creation and inheritance

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
        return "Name: {}, Account Number: {}".format(self.__name, self.__account_number)

    # Getters

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_amount_transferred(self):
        return self.__amount_transferred

    def get_name(self):
        return self.__name

    # Class Methods

    def deposit_money(self, amount):
        self.__balance += amount
        return self.__balance

    def transfer_money(self, amount):
        self.__balance -= int(amount)
        self.__amount_transferred += int(amount)
        return self.__balance


class CheckingAccount(Account):

    def __init__(self, name, account_number, balance=0):
        Account.__init__(self, name, account_number, balance)

    def __str__(self):
        return "Name: {}, Account Number: {}".format(self.get_name(), self.get_account_number())


class SavingsAccount(Account):

    __interest = 1.03

    def __init__(self, name, account_number, balance=0):
        Account.__init__(self, name, account_number, balance)

    def __str__(self):
        return "Name: {}, Account Number: {}".format(self.get_name, self.get_account_number())

    def calculate_interest_over_x_years(self, years):
        return (years * self.__interest) * self.get_balance()


class BusinessAccount(SavingsAccount):

    __business_name = ""
    __air_miles = 0

    def __init__(self, name, business_name, account_number, balance=1000):
        Account.__init__(self, name, account_number, balance)
        self.__business_name = business_name

    def __str__(self):
        return "Business Name: {}, Account Number: {}".format(self.__business_name, self.__air_miles)

    def calculate_air_miles(self):
        self.__air_miles = self.get_amount_transferred() * 0.01
        return self.__air_miles

    def get_air_miles(self):
        return self.__air_miles
