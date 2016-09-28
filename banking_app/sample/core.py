from sample import account


class Application:

    def __init__(self):
        user = self.open_app()

        while True:
            print("_" * 20)
            print("What would you like to do today?")
            print("[1] Transfer Money")
            print("[2] View Balance")
            print("[3] View Account Details")
            print("[9] Quit")
            user_choice = input(">> ")

            if user_choice == '1':
                print("_" * 20)
                print("How much would you like to transfer?")
                amount = input(">> ")
                user.transfer_money(amount)
                if user.get_balance() >= 0:
                    print("Thank you. Your remaining balance is £" + str(user.get_balance()))
                else:
                    print("Thank you. Your remaining balance is (-) £" + str(abs(user.get_balance())))
                input("")
            elif user_choice == '2':
                print("_" * 20)
                if user.get_balance() >= 0:
                    print("Thank you. Your remaining balance is £" + str(user.get_balance()))
                else:
                    print("Thank you. Your remaining balance is (-) £" + str(abs(user.get_balance())))
                input("")
            elif user_choice == '3':
                print("_" * 20)
                print(user)
                print("Your balance is: " + str(user.get_balance()))
                input("")
            elif user_choice == '9':
                break
            else:
                print("Invalid response. Main Menu restarting")
                input("")

        print("Goodbye.")
        input("")

    def open_app(self):
        print("Welcome to your Banking App")
        print("What type of account would you like to set up today?")
        print("[1] Checking Account, [2] Savings Account, [3] Business Account")
        user_choice = input(">> ")

        if user_choice == '1':
            print("You chose a 'Checking Account'.")
            print("We just need your name to get you set up.")
            name = input(">> ")
            user = account.CheckingAccount(name, 1)
            print("Thank you " + name + ". We have created your checking account")
        elif user_choice == '2':
            print("You chose a 'Savings Account'.")
            print("We just need your name to get you set up.")
            name = input(">> ")
            user = account.SavingsAccount(name, 1)
            print("Thank you " + name + ". We have created your savings account")
        elif user_choice == '3':
            print("You chose a 'Business Account'.")
            print("We just need your name and business name to get you set up.")
            name = input("Personal name >> ")
            business_name = input("Business name >> ")
            user = account.BusinessAccount(name, business_name, 1)
            print("Thank you " + name + ". Your account for " + business_name + " has been set up.")
        else:
            print("That was an invalid response. Application restarting.")
            input("")
            self.open_app()
        return user


def run_app():
    Application()


if __name__ == '__main__':
    run_app()
